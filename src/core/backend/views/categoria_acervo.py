from rest_framework.viewsets import ModelViewSet

from core.backend.models import CategoriaAcervo
from core.backend.serializers.categoria_acervo import CategoriaAcervoSerializer

class CategoriaAcervoViewSet(ModelViewSet):
    queryset = CategoriaAcervo.objects.all()
    serializer_class = CategoriaAcervoSerializer