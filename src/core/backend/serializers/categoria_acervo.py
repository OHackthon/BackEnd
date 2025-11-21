from rest_framework.serializers import ModelSerializer
from core.backend.models import CategoriaAcervo

class CategoriaAcervoSerializer(ModelSerializer):
    class Meta:
        model = CategoriaAcervo
        fields = '__all__'
