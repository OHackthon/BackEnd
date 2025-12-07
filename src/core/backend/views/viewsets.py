from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from core.backend.models import (
    CategoriaAcervo,
    Colecao,
    Item,
    Localizacao,
    MateriaPrima,
    SubtipoMaterial,
    Reserva,
)
from core.backend.serializers.categoriaAcervo import CategoriaAcervoSerializer
from core.backend.serializers.colecao import ColecaoSerializer
from core.backend.serializers.ItemAcervo import ItemSerializer
from core.backend.serializers.localizacao import LocalizacaoSerializer
from core.backend.serializers.materiaprima import MateriaPrimaSerializer
from core.backend.serializers.subTipo import SubtipoMaterialSerializer
from core.backend.serializers.user import UserSerializer
from core.backend.serializers.reserva import ReservaSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class CategoriaAcervoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAcervo.objects.all()
    serializer_class = CategoriaAcervoSerializer


class ColecaoViewSet(viewsets.ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    pagination_class = None


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer


class MateriaPrimaViewSet(viewsets.ModelViewSet):
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer


class SubtipoMaterialViewSet(viewsets.ModelViewSet):
    queryset = SubtipoMaterial.objects.all()
    serializer_class = SubtipoMaterialSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
