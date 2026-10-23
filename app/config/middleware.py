def client_ip(request):
    """Do not trust visitor-supplied X-Forwarded-For headers."""
    return request.META.get("REMOTE_ADDR", "")


class ResponsePolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Project templates and the installed admin use external scripts, including data attributes.
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data: blob:; media-src 'self' blob:; font-src 'self'; "
            "connect-src 'self'; object-src 'none'; base-uri 'self'; "
            "form-action 'self'; frame-ancestors 'none'"
        )
        if (
            request.path.startswith(("/staff/", "/account/"))
            or request.path.rstrip("/").endswith(("/contact", "/inquiry"))
            or request.method not in {"GET", "HEAD", "OPTIONS"}
        ):
            response.headers["Cache-Control"] = "no-store, private"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
        return response
