from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.backend.models import SubtipoMaterial
from core.backend.serializers.sub_tipo import SubTipoSerializer


class SubTipoViewSet(ModelViewSet):
    queryset = SubtipoMaterial.objects.all()
    serializer_class = SubTipoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
