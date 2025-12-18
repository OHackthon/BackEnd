from rest_framework import viewsets
from core.backend.models import Reserva
from core.backend.serializers import ReservaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
