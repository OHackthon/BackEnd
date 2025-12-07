from rest_framework import serializers
from core.backend.models import Reserva
from .ItemAcervo import ItemSerializer
from .localizacao import LocalizacaoSerializer
from .user import UserSerializer
class ReservaSerializer(serializers.ModelSerializer):
    item_data = ItemSerializer(source="item", read_only=True)
    local_origem_data = LocalizacaoSerializer(source="local_origem", read_only=True)
    local_destino_data = LocalizacaoSerializer(source="local_destino", read_only=True)
    responsavel_data = UserSerializer(source="responsavel", read_only=True)
    class Meta:
        model = Reserva
        fields = [
            "id",
            "item",
            "responsavel",
            "local_origem",
            "local_destino",
            "data_movimentacao",
            "tipo_movimento",
            "item_data",
            "local_origem_data",
            "local_destino_data",
            "responsavel_data",
        ]