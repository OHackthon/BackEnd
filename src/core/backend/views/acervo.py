from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from core.backend.models import Acervo
from core.backend.serializers.acervo import AcervoSerializer

class AcervoViewSet(ModelViewSet):
    queryset = Acervo.objects.all()
    serializer_class = AcervoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
