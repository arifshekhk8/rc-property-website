import uuid
from decimal import Decimal
from io import BytesIO

from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.validators import MinValueValidator
from django.db import models
from django.templatetags.static import static
from django.urls import reverse
from django.utils.translation import get_language
from PIL import Image, ImageOps, UnidentifiedImageError


def localized(instance, field):
    language = "bn" if (get_language() or "").startswith("bn") else "en"
    return getattr(instance, f"{field}_{language}") or getattr(instance, f"{field}_en")


class ProjectQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publication="published")


class Project(models.Model):
    class Publication(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        ARCHIVED = "archived", "Archived"

    class Availability(models.TextChoices):
        AVAILABLE = "available", "Available"
        UNAVAILABLE = "unavailable", "Unavailable"

    slug = models.SlugField(unique=True)
    title_en = models.CharField(max_length=120)
    title_bn = models.CharField(max_length=120)
    location_en = models.CharField(max_length=160)
    location_bn = models.CharField(max_length=160)
    description_en = models.TextField(max_length=1800, blank=True)
    description_bn = models.TextField(max_length=1800, blank=True)
    price_bdt = models.DecimalField(
        max_digits=14, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    area_katha = models.DecimalField(
        max_digits=9, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    area_sqft = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    publication = models.CharField(
        max_length=12, choices=Publication.choices, default=Publication.DRAFT
    )
    availability = models.CharField(
        max_length=12, choices=Availability.choices, default=Availability.AVAILABLE
    )
    is_sample = models.BooleanField(
        default=True,
        help_text="Keeps sample labels visible. Actual details/media must be reviewed before removing.",
    )
    sample_asset = models.CharField(
        max_length=40,
        choices=[("project-01", "Green sample"), ("project-02", "Sandy sample")],
        default="project-01",
    )
    order = models.PositiveSmallIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProjectQuerySet.as_manager()

    class Meta:
        ordering = ["order", "pk"]
        permissions = [("publish_project", "Can publish project content")]
        constraints = [
            models.CheckConstraint(condition=models.Q(price_bdt__gt=0), name="positive_price"),
            models.CheckConstraint(condition=models.Q(area_katha__gt=0), name="positive_katha"),
            models.CheckConstraint(condition=models.Q(area_sqft__gt=0), name="positive_sqft"),
        ]

    def __str__(self):
        return self.title_en

    @property
    def title(self):
        return localized(self, "title")

    @property
    def location(self):
        return localized(self, "location")

    @property
    def description(self):
        return localized(self, "description")

    @property
    def public_images(self):
        return [
            image
            for image in self.images.all()
            if image.rights_confirmed and image.approved_for_publication
        ]

    @property
    def additional_images(self):
        return self.public_images[1:]

    @property
    def cover_image(self):
        return next(iter(self.public_images), None)

    @property
    def cover_url(self):
        image = self.cover_image
        return image.public_url if image else static(f"images/{self.sample_asset}.webp")

    @property
    def cover_is_illustrative(self):
        return self.cover_image.illustrative if self.cover_image else True

    @property
    def cover_alt(self):
        return self.cover_image.alt if self.cover_image else self.cover_caption

    @property
    def cover_caption(self):
        if self.cover_image:
            return self.cover_image.caption
        label = "নমুনা চিত্র" if (get_language() or "").startswith("bn") else "Sample illustration"
        return f"{self.title} · {label}"

    def get_absolute_url(self):
        return reverse("project_detail", args=[self.slug])

    @property
    def sample_video_url(self):
        return static(f"images/{self.sample_asset}-sample.mp4")


def image_path(instance, filename):
    return f"project-images/{instance.id}.jpg"


class ProjectImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=image_path)
    caption_en = models.CharField(max_length=180)
    caption_bn = models.CharField(max_length=180)
    alt_en = models.CharField(max_length=240)
    alt_bn = models.CharField(max_length=240)
    illustrative = models.BooleanField(default=True)
    rights_confirmed = models.BooleanField(default=False)
    approved_for_publication = models.BooleanField(
        default=False, help_text="A permitted publisher must approve this image for public display."
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "pk"]

    @property
    def caption(self):
        return localized(self, "caption")

    @property
    def alt(self):
        return localized(self, "alt")

    @property
    def public_url(self):
        return reverse("project_image", args=[self.pk])

    @property
    def is_public(self):
        return (
            self.project.publication == Project.Publication.PUBLISHED
            and self.rights_confirmed
            and self.approved_for_publication
        )

    def clean(self):
        super().clean()
        if not self.image or self.image._committed:
            return
        if self.image.size > 10 * 1024 * 1024:
            raise ValidationError({"image": "Use an image under 10 MB."})
        try:
            with Image.open(self.image) as im:
                if im.format not in ("JPEG", "PNG", "WEBP") or im.width * im.height > 24_000_000:
                    raise ValidationError({"image": "Use a JPEG, PNG or WebP up to 24 megapixels."})
                im.verify()
        except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as exc:
            raise ValidationError({"image": "The image could not be validated."}) from exc
        finally:
            self.image.seek(0)

    def save(self, *args, **kwargs):
        if self.image and not self.image._committed:
            self.clean()
            with Image.open(self.image) as im:
                normalized = ImageOps.exif_transpose(im).convert("RGB")
                normalized.thumbnail((2400, 2400))
                buffer = BytesIO()
                normalized.save(buffer, format="JPEG", quality=87, optimize=True)
            self.image = ContentFile(buffer.getvalue(), name=f"{self.id}.jpg")
        super().save(*args, **kwargs)


class FAQ(models.Model):
    question_en = models.CharField(max_length=200)
    question_bn = models.CharField(max_length=200)
    answer_en = models.TextField(max_length=1200)
    answer_bn = models.TextField(max_length=1200)
    published = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "pk"]

    @property
    def question(self):
        return localized(self, "question")

    @property
    def answer(self):
        return localized(self, "answer")

    def __str__(self):
        return self.question_en
