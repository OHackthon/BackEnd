"""
Middleware para permitir requisições sem validação de HOST
"""


class BypassHostValidationMiddleware:
    """Bypass HOST validation para production"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Se o HOST vem vazio ou localhost, aceita
        host = request.META.get("HTTP_HOST", "")
        if not host or host in ["127.0.0.1:10000", "localhost", "localhost:8000"]:
            request.META["HTTP_HOST"] = "localhost"
        return self.get_response(request)
        return self.get_response(request)
