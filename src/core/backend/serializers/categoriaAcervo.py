from rest_framework import serializers
from core.backend.models import CategoriaAcervo
class CategoriaAcervoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source="nome_categoria")
    class Meta:
        model = CategoriaAcervo
        fields = ["id", "nome", "descricao"]