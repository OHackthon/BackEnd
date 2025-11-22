from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.backend.models import Localizacao
from core.backend.serializers.localizacao import LocalizacaoSerializer


class LocalizacaoViewSet(ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Permite leitura pública
