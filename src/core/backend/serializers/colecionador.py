from rest_framework.serializers import ModelSerializer

from core.backend.models import Colecionador

class ColecionadorSerializer(ModelSerializer):
    class Meta:
        model = Colecionador
        fields = '__all__'