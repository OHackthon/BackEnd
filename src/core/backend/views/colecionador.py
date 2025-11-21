from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.backend.models import Colecionador
from core.backend.serializers.colecionador import ColecionadorSerializer

class ColecionadorViewSet(ModelViewSet):
    queryset = Colecionador.objects.all()
    serializer_class = ColecionadorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
