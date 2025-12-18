from rest_framework import viewsets
from core.backend.models import CategoriaAcervo
from core.backend.serializers import CategoriaAcervoSerializer


class CategoriaAcervoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAcervo.objects.all()
    serializer_class = CategoriaAcervoSerializer
