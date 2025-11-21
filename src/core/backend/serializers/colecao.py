from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.backend.models import Colecao


class ColecaoSerializer(ModelSerializer):
    quantidade_itens = SerializerMethodField()
    tem_itens = SerializerMethodField()

    def get_quantidade_itens(self, obj):
        return obj.item_set.count()

    def get_tem_itens(self, obj):
        return obj.item_set.exists()

    class Meta:
        model = Colecao
        fields = "__all__"
