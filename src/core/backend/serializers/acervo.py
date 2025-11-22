from rest_framework.serializers import  ModelSerializer

from core.backend.models import Acervo

class AcervoSerializer(ModelSerializer):
    class Meta:
        model = Acervo
        fields = '__all__'