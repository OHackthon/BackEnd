from rest_framework import serializers
from ..models.materiaPrima import MateriaPrima
class MateriaPrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MateriaPrima
        fields = "__all__"