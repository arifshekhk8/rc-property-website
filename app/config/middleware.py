def client_ip(request):
    """Do not trust visitor-supplied X-Forwarded-For headers."""
    return request.META.get("REMOTE_ADDR", "")


class ResponsePolicyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Django admin uses its own inline-script conventions; keep the public app strict.
        if not request.path.startswith(("/staff/", "/account/")):
            response.headers["Content-Security-Policy"] = (
                "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; "
                "img-src 'self' data: blob:; media-src 'self' blob:; font-src 'self'; "
                "connect-src 'self'; object-src 'none'; base-uri 'self'; "
                "form-action 'self'; frame-ancestors 'none'"
            )
        else:
            response.headers["Cache-Control"] = "no-store, private"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
        return response
