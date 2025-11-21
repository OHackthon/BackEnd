from rest_framework.viewsets import ModelViewSet

from core.backend.models import subTipo
from core.backend.serializers import SubTipoSerializer

class SubTipoViewSet(ModelViewSet):
    queryset = subTipo.objects.all()
    serializer_class = SubTipoSerializer

