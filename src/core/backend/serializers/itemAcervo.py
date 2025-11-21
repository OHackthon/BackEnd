from rest_framework.serializers import ModelSerializer
from core.backend.models import Item

class ItemAcervoSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'