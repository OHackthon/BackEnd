from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from core.backend.models import MateriaPrima
from core.backend.serializers.materia_prima import MateriaPrimaSerializer


class MateriaPrimaViewSet(ModelViewSet):
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
