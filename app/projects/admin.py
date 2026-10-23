from django.contrib import admin
from django.core.exceptions import PermissionDenied

from .models import FAQ, Project, ProjectImage


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 0
    fields = [
        "image",
        ("caption_en", "caption_bn"),
        ("alt_en", "alt_bn"),
        ("illustrative", "rights_confirmed", "order"),
    ]


class PublishedContentGuardMixin:
    """Publication authority also governs destructive changes to live content."""

    live_filter = {}

    def can_mutate(self, request, obj):
        return (
            obj is None
            or not all(getattr(obj, key) == value for key, value in self.live_filter.items())
            or request.user.has_perm("projects.publish_project")
        )

    def has_change_permission(self, request, obj=None):
        return super().has_change_permission(request, obj) and self.can_mutate(request, obj)

    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj) and self.can_mutate(request, obj)

    def delete_model(self, request, obj):
        if not self.can_mutate(request, obj):
            raise PermissionDenied
        super().delete_model(request, obj)

    def delete_queryset(self, request, queryset):
        if (
            not request.user.has_perm("projects.publish_project")
            and queryset.filter(**self.live_filter).exists()
        ):
            raise PermissionDenied
        super().delete_queryset(request, queryset)


@admin.register(Project)
class ProjectAdmin(PublishedContentGuardMixin, admin.ModelAdmin):
    live_filter = {"publication": "published"}
    list_display = [
        "title_en",
        "publication",
        "availability",
        "price_bdt",
        "is_sample",
        "updated_at",
    ]
    list_filter = ["publication", "availability", "is_sample"]
    search_fields = ["title_en", "title_bn"]
    prepopulated_fields = {"slug": ["title_en"]}
    inlines = [ProjectImageInline]
    fieldsets = [
        ("English", {"fields": ["title_en", "location_en", "description_en"]}),
        ("বাংলা", {"fields": ["title_bn", "location_bn", "description_bn"]}),
        ("Project facts", {"fields": ["price_bdt", "area_katha", "area_sqft", "availability"]}),
        (
            "Publication",
            {
                "fields": ["publication", "is_sample", "slug", "order", "sample_asset"],
                "description": "This foundation edits the current record directly. A separate draft-revision/review workflow is a later milestone. Keep sample labeling until facts and media are approved.",
            },
        ),
    ]

    def get_readonly_fields(self, request, obj=None):
        if not request.user.has_perm("projects.publish_project"):
            return ["publication"]
        return []

    def save_model(self, request, obj, form, change):
        if obj.publication == "published" and not request.user.has_perm("projects.publish_project"):
            raise PermissionDenied
        super().save_model(request, obj, form, change)


@admin.register(FAQ)
class FAQAdmin(PublishedContentGuardMixin, admin.ModelAdmin):
    live_filter = {"published": True}
    list_display = ["question_en", "published", "order"]
    fields = ["question_en", "answer_en", "question_bn", "answer_bn", "order", "published"]

    def get_readonly_fields(self, request, obj=None):
        return [] if request.user.has_perm("projects.publish_project") else ["published"]
