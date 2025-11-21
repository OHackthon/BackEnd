from rest_framework.viewsets import ModelViewSet

from core.backend.models import Item
from core.backend.serializers import ItemAcervoSerializer


class ItemAcervoViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemAcervoSerializer
