from rest_framework.viewsets import ModelViewSet

from core.backend.models import itemAcervo
from core.backend.serializers import ItemAcervoSerializer

class ItemAcervoViewSet(ModelViewSet):
    queryset = itemAcervo.objects.all()
    serializer_class = ItemAcervoSerializer