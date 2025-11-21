from rest_framework.viewsets import ModelViewSet

from core.backend.models import Localizacao
from core.backend.serializers import LocalizacaoSerializer

class LocalizacaoViewSet(ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer