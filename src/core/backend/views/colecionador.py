from rest_framework.viewsets import ModelViewSet

from core.backend.models import Colecionador
from core.backend.serializers import ColecionadorSerializer

class ColecionadorViewSet(ModelViewSet):
    queryset = Colecionador.objects.all()
    serializer_class = ColecionadorSerializer