from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from core.backend.models import Colecionador
from core.backend.serializers.colecionador import ColecionadorSerializer

from core.backend.models import Colecao


class ColecaoSerializer(ModelSerializer):
    colecionador = serializers.PrimaryKeyRelatedField(
        queryset=Colecionador.objects.all()
    )
    colecionador_data = ColecionadorSerializer(source="colecionador", read_only=True)
    quantidade_itens = SerializerMethodField()
    tem_itens = SerializerMethodField()

    def get_quantidade_itens(self, obj):
        return obj.item_set.count()

    def get_tem_itens(self, obj):
        return obj.item_set.exists()

    class Meta:
        model = Colecao
        fields = [
            "id",
            "nome_colecao",
            "descricao",
            "colecionador",
            "quantidade_itens",
            "data_registro",
            "tem_itens",
            "colecionador_data",
        ]
        depth = 1
