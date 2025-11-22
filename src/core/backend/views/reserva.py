from rest_framework.viewsets import ModelViewSet
from core.backend.models import Reserva
from core.backend.serializers.reserva import ReservaSerializer


class ReservaViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)