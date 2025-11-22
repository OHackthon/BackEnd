from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.backend.models import Colecao
from core.backend.serializers.colecao import ColecaoSerializer

class ColecaoViewSet(ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
