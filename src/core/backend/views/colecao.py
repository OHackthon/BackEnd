from rest_framework.viewsets import ModelViewSet

from core.backend.models import Colecao
from core.backend.serializers import ColecaoSerializer


class ColecaoViewSet(ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
