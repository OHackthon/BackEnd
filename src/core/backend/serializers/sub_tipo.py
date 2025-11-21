from rest_framework.serializers import ModelSerializer
from core.backend.models import SubtipoMaterial

class SubTipoSerializer(ModelSerializer):
    class Meta:
        model = SubtipoMaterial
        fields = "__all__"
