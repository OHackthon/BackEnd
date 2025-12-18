from rest_framework import viewsets
from core.backend.models import Localizacao
from core.backend.serializers import LocalizacaoSerializer


class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
