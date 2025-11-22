from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from core.backend.models import Item
from core.backend.serializers.item_acervo import ItemAcervoSerializer
from core.backend.serializers.localizacao import LocalizacaoSerializer

from core.backend.models import Reserva


class ReservaSerializer(ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    item_data = ItemAcervoSerializer(source="item", read_only=True)
    local_origem_data = LocalizacaoSerializer(source="local_origem", read_only=True)
    local_destino_data = LocalizacaoSerializer(source="local_destino", read_only=True)
    responsavel_data = serializers.StringRelatedField(source="responsavel", read_only=True)

    class Meta:
        model = Reserva
        fields = (
            "id",
            "data_movimentacao",
            "tipo_movimento",
            "item",
            "item_data",
            "responsavel",
            "local_origem",
            "local_destino",
            "local_origem_data",
            "local_destino_data",
            'responsavel_data',
        )
        read_only_fields = ("responsavel",)
