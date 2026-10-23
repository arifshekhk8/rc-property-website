from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404

from .models import ProjectImage


def project_image(request, image_id):
    image = get_object_or_404(ProjectImage.objects.select_related("project"), pk=image_id)
    can_preview = (
        request.user.is_authenticated
        and request.user.is_staff
        and request.user.is_verified()
        and request.user.has_perm("projects.view_projectimage")
    )
    if image.project.publication != "published" and not can_preview:
        raise Http404
    try:
        response = FileResponse(image.image.open("rb"), content_type="image/jpeg")
    except FileNotFoundError as exc:
        raise Http404 from exc
    response["Cache-Control"] = (
        "private, no-store" if image.project.publication != "published" else "no-cache"
    )
    return response
