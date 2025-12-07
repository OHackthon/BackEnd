from rest_framework.serializers import ModelSerializer
from core.backend.models import Localizacao
class LocalizacaoSerializer(ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'