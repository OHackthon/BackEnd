"""
Middleware para permitir requisições sem validação de HOST
"""

class HealthCheckMiddleware:
    """Permite /health/ sem validação de HOST"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Pula validação de HOST para health check
        if request.path == '/health/':
            request.META['HTTP_HOST'] = 'localhost'
        return self.get_response(request)
