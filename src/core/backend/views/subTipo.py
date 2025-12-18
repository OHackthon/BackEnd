from rest_framework import viewsets
from core.backend.models import SubtipoMaterial
from core.backend.serializers import SubtipoMaterialSerializer


class SubtipoMaterialViewSet(viewsets.ModelViewSet):
    queryset = SubtipoMaterial.objects.all()
    serializer_class = SubtipoMaterialSerializer
