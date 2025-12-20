"""
Middleware para forçar HOST válido antes de qualquer validação Django
"""


class ForceValidHostMiddleware:
    """Força um HOST válido antes de Django validar"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Se não tem HTTP_HOST ou é vazio, força localhost
        host = request.META.get("HTTP_HOST", "")
        if not host or ":" in host and not host.startswith("localhost"):
            # Se vem um IP:PORT que não é localhost, força localhost
            request.META["HTTP_HOST"] = "localhost"
            request.META["SERVER_NAME"] = "localhost"
        return self.get_response(request)
