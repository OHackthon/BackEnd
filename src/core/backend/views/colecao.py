from rest_framework import viewsets
from core.backend.models import Colecao
from core.backend.serializers import ColecaoSerializer


class ColecaoViewSet(viewsets.ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    pagination_class = None
