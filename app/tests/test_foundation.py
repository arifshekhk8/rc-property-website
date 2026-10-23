import tempfile
from decimal import Decimal
from io import BytesIO, StringIO

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.db import IntegrityError, connection, transaction
from django.test import Client, TestCase, override_settings
from django.test.utils import CaptureQueriesContext
from django_otp import DEVICE_ID_SESSION_KEY
from django_otp.plugins.otp_totp.models import TOTPDevice
from PIL import Image, PngImagePlugin
from projects.models import FAQ, Project, ProjectImage
from website.forms import InquiryForm


class PublicBoundaryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_demo", stdout=StringIO())
        cls.first = Project.objects.get(slug="project-01")
        cls.draft = Project.objects.create(
            slug="private-draft",
            title_en="DO NOT PUBLISH THIS DRAFT",
            title_bn="অপ্রকাশিত",
            location_en="Private location",
            location_bn="অপ্রকাশিত",
            price_bdt=1,
            area_katha=1,
            area_sqft=1,
            publication="draft",
        )

    def test_all_public_pages_render_in_both_languages(self):
        paths = [
            "",
            "projects/",
            "projects/project-01/",
            "projects/project-02/",
            "gallery/",
            "visit/",
            "visit/?mode=panorama",
            "about/",
            "contact/",
            "inquiry/",
            "privacy/",
            "terms/",
        ]
        for language in ["en", "bn"]:
            for path in paths:
                with self.subTest(language=language, path=path):
                    response = self.client.get(f"/{language}/{path}")
                    self.assertEqual(response.status_code, 200)
                    self.assertNotContains(response, self.draft.title_en)
                    self.assertContains(response, f'lang="{language}"')

    def test_bangla_content_and_exact_sample_facts(self):
        response = self.client.get("/bn/projects/project-01/")
        self.assertContains(response, "প্রকল্প 01")
        self.assertContains(response, "৳45,00,000")
        self.assertContains(response, "2,160")
        self.assertContains(response, "বর্গফুট")

    def test_language_switch_preserves_project_and_query(self):
        response = self.client.get("/en/visit/?project=project-02&mode=panorama")
        self.assertContains(response, "/bn/visit/?project=project-02&amp;mode=panorama")

    def test_unpublished_records_are_unavailable_by_direct_url_or_media_selector(self):
        for language in ["en", "bn"]:
            self.assertEqual(
                self.client.get(f"/{language}/projects/private-draft/").status_code, 404
            )
            self.assertEqual(
                self.client.get(f"/{language}/visit/?project=private-draft").status_code, 404
            )
            self.assertEqual(
                self.client.get(f"/{language}/inquiry/?project=private-draft").status_code, 404
            )

    def test_archiving_removes_the_record_from_browsing_and_guide(self):
        self.first.publication = "archived"
        self.first.save()
        self.assertNotContains(self.client.get("/en/"), "Project 01")
        self.assertEqual(self.client.get("/en/projects/project-01/").status_code, 404)

    def test_staff_content_is_escaped_in_public_markup(self):
        self.first.title_en = '<script>alert("unsafe")</script>'
        self.first.save()
        response = self.client.get("/en/projects/")
        self.assertNotContains(response, '<script>alert("unsafe")</script>')
        self.assertContains(response, "&lt;script&gt;")

    def test_sample_seed_never_overwrites_staff_changes(self):
        self.first.price_bdt = Decimal("1234567")
        self.first.save()
        call_command("seed_demo", stdout=StringIO())
        self.first.refresh_from_db()
        self.assertEqual(self.first.price_bdt, Decimal("1234567"))
        self.assertEqual(Project.objects.filter(slug__in=["project-01", "project-02"]).count(), 2)

    def test_inquiry_requires_consent_and_excludes_draft_project_ids(self):
        valid = {"phone": "01700000000", "project": self.first.pk, "consent": True}
        self.assertTrue(InquiryForm(valid).is_valid())
        self.assertFalse(InquiryForm({**valid, "consent": False}).is_valid())
        self.assertFalse(InquiryForm({**valid, "project": self.draft.pk}).is_valid())

    def test_bangla_phone_digits_are_normalized(self):
        form = InquiryForm({"phone": "+৮৮০১৭০০০০০০০০", "project": self.first.pk, "consent": True})
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data["phone"], "01700000000")

    def test_demo_inquiry_never_writes_contact_details(self):
        with CaptureQueriesContext(connection) as queries:
            response = self.client.post(
                "/en/inquiry/",
                {
                    "name": "Synthetic visitor",
                    "phone": "01700000000",
                    "project": self.first.pk,
                    "message": "Sample only",
                    "consent": "on",
                },
            )
        self.assertContains(response, "Your details were not stored")
        self.assertNotContains(response, "01700000000")
        self.assertFalse(
            any(q["sql"].lstrip().upper().startswith(("INSERT", "UPDATE")) for q in queries)
        )

    def test_inquiry_and_staff_login_require_csrf(self):
        client = Client(enforce_csrf_checks=True)
        self.assertEqual(client.post("/en/inquiry/", {"phone": "01700000000"}).status_code, 403)
        self.assertEqual(
            client.post("/account/login/", {"auth-username": "nobody"}).status_code, 403
        )

    def test_public_security_headers(self):
        response = self.client.get("/en/")
        self.assertIn("script-src 'self';", response["Content-Security-Policy"])
        self.assertNotIn(
            "unsafe-inline",
            response["Content-Security-Policy"].split("script-src")[1].split(";")[0],
        )
        self.assertEqual(response["X-Frame-Options"], "DENY")
        self.assertEqual(response["X-Content-Type-Options"], "nosniff")

    def test_database_rejects_non_positive_price_and_area(self):
        for field in ["price_bdt", "area_katha", "area_sqft"]:
            with self.subTest(field=field):
                with self.assertRaises(IntegrityError), transaction.atomic():
                    Project.objects.filter(pk=self.first.pk).update(**{field: 0})


class StaffBoundaryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("seed_demo", stdout=StringIO())
        cls.project = Project.objects.get(slug="project-01")
        cls.manager = get_user_model().objects.create_user("test-manager", is_staff=True)
        cls.editor = get_user_model().objects.create_user("test-editor", is_staff=True)
        cls.manager.user_permissions.set(
            Permission.objects.filter(content_type__app_label="projects")
        )
        cls.editor.user_permissions.set(
            Permission.objects.filter(codename__in=["view_project", "change_project"])
        )
        cls.manager_device = TOTPDevice.objects.create(
            user=cls.manager, name="test-device", confirmed=True
        )
        cls.editor_device = TOTPDevice.objects.create(
            user=cls.editor, name="test-device", confirmed=True
        )

    def verified(self, user, device):
        self.client.force_login(user, backend="django.contrib.auth.backends.ModelBackend")
        session = self.client.session
        session[DEVICE_ID_SESSION_KEY] = device.persistent_id
        session.save()

    def test_password_only_session_cannot_read_or_change_admin(self):
        self.client.force_login(self.manager, backend="django.contrib.auth.backends.ModelBackend")
        for url in [
            "/staff/",
            "/staff/projects/project/",
            f"/staff/projects/project/{self.project.pk}/change/",
        ]:
            self.assertEqual(self.client.get(url).status_code, 302)
        self.assertEqual(
            self.client.post(
                f"/staff/projects/project/{self.project.pk}/change/", {"title_en": "bypass"}
            ).status_code,
            302,
        )
        self.project.refresh_from_db()
        self.assertEqual(self.project.title_en, "Project 01")

    def test_admin_login_redirects_to_mfa_flow(self):
        response = self.client.get("/staff/login/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/account/login/"))
        self.assertEqual(self.client.get("/account/login/").status_code, 200)

    def test_verified_editor_cannot_modify_published_record(self):
        self.verified(self.editor, self.editor_device)
        response = self.client.post(
            f"/staff/projects/project/{self.project.pk}/change/", {"title_en": "bypass"}
        )
        self.assertEqual(response.status_code, 403)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title_en, "Project 01")

    def test_editor_cannot_delete_live_projects_or_faqs_even_with_delete_permission(self):
        self.editor.user_permissions.add(
            *Permission.objects.filter(
                content_type__app_label="projects",
                codename__in=["delete_project", "view_faq", "change_faq", "delete_faq"],
            )
        )
        self.verified(self.editor, self.editor_device)
        faq = FAQ.objects.get(published=True)
        for model, instance in [("project", self.project), ("faq", faq)]:
            with self.subTest(model=model):
                response = self.client.post(
                    f"/staff/projects/{model}/{instance.pk}/delete/", {"post": "yes"}
                )
                self.assertEqual(response.status_code, 403)
                response = self.client.post(
                    f"/staff/projects/{model}/",
                    {"action": "delete_selected", "_selected_action": [instance.pk], "post": "yes"},
                )
                self.assertEqual(response.status_code, 403)
                self.assertTrue(type(instance).objects.filter(pk=instance.pk).exists())

    def test_editor_with_delete_permission_can_delete_an_unpublished_draft(self):
        self.editor.user_permissions.add(Permission.objects.get(codename="delete_project"))
        self.project.publication = "draft"
        self.project.save()
        self.verified(self.editor, self.editor_device)
        response = self.client.post(
            f"/staff/projects/project/{self.project.pk}/delete/", {"post": "yes"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Project.objects.filter(pk=self.project.pk).exists())

    def test_verified_manager_can_edit_project_and_public_page_updates(self):
        self.verified(self.manager, self.manager_device)
        response = self.client.post(
            f"/staff/projects/project/{self.project.pk}/change/",
            {
                "title_en": "Updated sample project",
                "title_bn": "হালনাগাদ প্রকল্প",
                "location_en": "Dhaka · Sample location",
                "location_bn": "ঢাকা · নমুনা অবস্থান",
                "description_en": "Sample description",
                "description_bn": "নমুনা বিবরণ",
                "price_bdt": "4500000.00",
                "area_katha": "3.00",
                "area_sqft": "2160.00",
                "publication": "published",
                "availability": "available",
                "is_sample": "on",
                "slug": "project-01",
                "sample_asset": "project-01",
                "order": "1",
                "images-TOTAL_FORMS": "0",
                "images-INITIAL_FORMS": "0",
                "images-MIN_NUM_FORMS": "0",
                "images-MAX_NUM_FORMS": "1000",
                "_save": "Save",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertContains(self.client.get("/en/projects/project-01/"), "Updated sample project")
        self.assertContains(self.client.get("/bn/projects/project-01/"), "হালনাগাদ প্রকল্প")

    def test_revoked_mfa_device_removes_admin_access(self):
        self.verified(self.manager, self.manager_device)
        self.assertEqual(self.client.get("/staff/").status_code, 200)
        self.manager_device.delete()
        self.assertEqual(self.client.get("/staff/").status_code, 302)


class MediaBoundaryTests(TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.override = override_settings(MEDIA_ROOT=self.temp.name)
        self.override.enable()
        self.addCleanup(self.override.disable)
        self.addCleanup(self.temp.cleanup)
        call_command("seed_demo", stdout=StringIO())
        self.project = Project.objects.get(slug="project-01")

    def make_image(self):
        buffer = BytesIO()
        metadata = PngImagePlugin.PngInfo()
        metadata.add_text("PrivateComment", "strip-this-test-metadata")
        Image.new("RGB", (100, 70), "green").save(buffer, "PNG", pnginfo=metadata)
        return ProjectImage.objects.create(
            project=self.project,
            image=SimpleUploadedFile("untrusted.png", buffer.getvalue(), "image/png"),
            caption_en="Sample",
            caption_bn="নমুনা",
            alt_en="Sample",
            alt_bn="নমুনা",
        )

    def test_uploaded_photo_is_reencoded_and_metadata_removed(self):
        image = self.make_image()
        with image.image.open("rb") as stream:
            with Image.open(stream) as im:
                self.assertEqual(im.format, "JPEG")
                self.assertNotIn("PrivateComment", im.info)
        response = self.client.get(image.public_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "image/jpeg")

    def test_draft_media_cannot_be_read_anonymously(self):
        image = self.make_image()
        self.project.publication = "draft"
        self.project.save()
        self.assertEqual(self.client.get(image.public_url).status_code, 404)

    def test_active_content_disguised_as_photo_is_rejected(self):
        image = ProjectImage(
            project=self.project,
            image=SimpleUploadedFile("fake.png", b'<svg onload="alert(1)"></svg>', "image/png"),
        )
        with self.assertRaises(ValidationError):
            image.save()
