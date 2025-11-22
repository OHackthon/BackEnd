from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.backend.models import Item
from core.backend.serializers.item_acervo import ItemAcervoSerializer

class ItemAcervoViewSet(ModelViewSet):
    queryset = Item.objects.select_related(
        "colecao",
        "materia_prima",
        "subtipo",
        "localizacao_atual",
        "categoria_acervo",
        "acervo",
        "criado_por",
    ).all()
    serializer_class = ItemAcervoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
