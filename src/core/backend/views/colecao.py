from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from core.backend.models import Colecao
from core.backend.serializers.colecao import ColecaoSerializer

class ColecaoViewSet(ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']