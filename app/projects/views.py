from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_safe

from .models import ProjectImage


@require_safe
def project_image(request, image_id):
    image = get_object_or_404(ProjectImage.objects.select_related("project"), pk=image_id)
    can_preview = (
        request.user.is_authenticated
        and request.user.is_staff
        and request.user.is_verified()
        and request.user.has_perm("projects.view_projectimage")
    )
    if not image.is_public and not can_preview:
        raise Http404
    try:
        response = FileResponse(image.image.open("rb"), content_type="image/jpeg")
    except FileNotFoundError as exc:
        raise Http404 from exc
    response["Cache-Control"] = "no-cache" if image.is_public else "private, no-store"
    return response
