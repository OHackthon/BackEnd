from rest_framework.viewsets import ModelViewSet

from core.backend.models import SubtipoMaterial
from core.backend.serializers import SubTipoSerializer


class SubTipoViewSet(ModelViewSet):
    queryset = SubtipoMaterial.objects.all()
    serializer_class = SubTipoSerializer
