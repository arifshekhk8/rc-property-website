from django.urls import reverse, translate_url
from projects.models import Project

from .copy import BN, EN


def site_context(request):
    language = "bn" if getattr(request, "LANGUAGE_CODE", "en") == "bn" else "en"
    return {
        "copy": BN if language == "bn" else EN,
        "language": language,
        "other_language": "en" if language == "bn" else "bn",
        "other_language_label": "English" if language == "bn" else "বাংলা",
        "language_url": translate_url(request.get_full_path(), "en" if language == "bn" else "bn"),
        "guide_projects": Project.objects.published().only("title_en", "title_bn", "slug"),
        "home_url": reverse("home"),
    }
