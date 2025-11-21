from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.backend.models import CategoriaAcervo
from core.backend.serializers.categoria_acervo import CategoriaAcervoSerializer


class CategoriaAcervoViewSet(ModelViewSet):
    queryset = CategoriaAcervo.objects.all()
    serializer_class = CategoriaAcervoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
