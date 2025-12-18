from rest_framework import viewsets
from core.backend.models import MateriaPrima
from core.backend.serializers import MateriaPrimaSerializer


class MateriaPrimaViewSet(viewsets.ModelViewSet):
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer
