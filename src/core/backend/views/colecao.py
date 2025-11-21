import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Exists, OuterRef

from core.backend.models import Colecao, Item
from core.backend.serializers.colecao import ColecaoSerializer


class ColecaoFilter(django_filters.FilterSet):
    tem_itens = django_filters.BooleanFilter(method="filter_tem_itens")

    def filter_tem_itens(self, queryset, name, value):
        if value is True:
            # Filtra coleções que têm pelo menos um item
            return queryset.filter(item__isnull=False).distinct()
        elif value is False:
            # Filtra coleções que não têm itens
            return queryset.filter(item__isnull=True)
        return queryset

    class Meta:
        model = Colecao
        fields = {
            "nome_colecao": ["exact", "icontains"],
            "colecionador": ["exact"],
        }


class ColecaoViewSet(ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ColecaoFilter
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]  # Permite leitura pública, escrita apenas autenticada
