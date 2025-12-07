from rest_framework.serializers import ModelSerializer
from core.backend.models import Item
from .colecao import ColecaoSerializer
from .materiaprima import MateriaPrimaSerializer
from .subTipo import SubtipoMaterialSerializer
from .localizacao import LocalizacaoSerializer
from .categoriaAcervo import CategoriaAcervoSerializer
class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            if instance.colecao:
                representation["colecao"] = ColecaoSerializer(instance.colecao).data
        except:
            pass
        try:
            if instance.materia_prima:
                representation["materia_prima"] = MateriaPrimaSerializer(
                    instance.materia_prima
                ).data
        except:
            pass
        try:
            if instance.subtipo:
                representation["subtipo"] = SubtipoMaterialSerializer(
                    instance.subtipo
                ).data
        except:
            pass
        try:
            if instance.localizacao_atual:
                representation["localizacao_atual"] = LocalizacaoSerializer(
                    instance.localizacao_atual
                ).data
        except:
            pass
        try:
            if instance.categoria_acervo:
                representation["categoria_acervo"] = CategoriaAcervoSerializer(
                    instance.categoria_acervo
                ).data
        except:
            pass
        return representation