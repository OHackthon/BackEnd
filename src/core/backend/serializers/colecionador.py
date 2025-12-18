from rest_framework import serializers
from core.backend.models import Colecionador


class ColecionadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colecionador
        fields = [
            "id",
            "nome",
            "data_nascimento",
            "email",
            "telefone",
            "endereco",
            "data_registro_sistema",
        ]
        read_only_fields = ["id", "data_registro_sistema"]
