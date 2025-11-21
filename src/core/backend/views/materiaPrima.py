from rest_framwork.viewsets import ModelViewSet
from core.backend.models import MateriaPrima

from core.backend.models import MateriaPrima
from core.backend.serializers import MateriaPrimaSerializer

class MateriaPrimaViewSet(ModelViewSet):
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer
