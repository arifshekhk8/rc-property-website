from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_GET, require_http_methods
from projects.models import Project

from .forms import InquiryForm


def published_projects():
    return Project.objects.published().prefetch_related("images")


@require_GET
def home(request):
    return render(
        request, "website/home.html", {"projects": published_projects(), "active": "home"}
    )


@require_GET
def projects(request):
    return render(
        request, "website/projects.html", {"projects": published_projects(), "active": "projects"}
    )


@require_GET
def project_detail(request, slug):
    project = get_object_or_404(published_projects(), slug=slug)
    return render(
        request, "website/project_detail.html", {"project": project, "active": "projects"}
    )


@require_GET
def gallery(request):
    return render(
        request, "website/gallery.html", {"projects": published_projects(), "active": "gallery"}
    )


@require_GET
def virtual_visit(request):
    queryset = published_projects()
    slug = request.GET.get("project")
    project = get_object_or_404(queryset, slug=slug) if slug else queryset.first()
    mode = "panorama" if request.GET.get("mode") == "panorama" else "video"
    return render(
        request,
        "website/visit.html",
        {"project": project, "projects": queryset, "mode": mode, "active": "projects"},
    )


@require_GET
def about(request):
    return render(request, "website/about.html", {"active": "about"})


@sensitive_post_parameters()
@require_http_methods(["GET", "POST"])
def contact(request):
    return inquiry(request, contact_page=True)


@sensitive_post_parameters()
@require_http_methods(["GET", "POST"])
def inquiry(request, contact_page=False):
    # Foundation preview only: never store, log or send form fields, even when submitted.
    slug = request.GET.get("project")
    initial = {}
    if slug:
        initial["project"] = get_object_or_404(Project.objects.published(), slug=slug)
    form = InquiryForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        return render(
            request,
            "website/receipt.html",
            {"project": form.cleaned_data["project"], "demo": True, "active": "contact"},
        )
    return render(
        request,
        "website/contact.html",
        {"form": form, "contact_page": contact_page, "active": "contact", "demo": True},
        status=422 if request.method == "POST" else 200,
    )


@require_GET
def privacy(request):
    return render(request, "website/policy.html", {"policy": "privacy"})


@require_GET
def terms(request):
    return render(request, "website/policy.html", {"policy": "terms"})


@require_GET
def health(request):
    return HttpResponse("ok", content_type="text/plain")
