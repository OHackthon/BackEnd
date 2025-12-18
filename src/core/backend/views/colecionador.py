from rest_framework import viewsets
from core.backend.models import Colecionador
from core.backend.serializers import ColecionadorSerializer


class ColecionadorViewSet(viewsets.ModelViewSet):
    queryset = Colecionador.objects.all()
    serializer_class = ColecionadorSerializer
