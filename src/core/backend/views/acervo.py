from rest_framework.viewsets import ModelViewSet

from core.backend.models import Acervo
from core.backend.serializers import AcervoSerializer

class AcervoViewSet(ModelViewSet):
    queryset = Acervo.objects.all()
    serializer_class = AcervoSerializer