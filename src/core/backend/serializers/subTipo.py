from rest_framework.serializers import ModelSerializer
from core.backend.models import Item

class SubTipoSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'