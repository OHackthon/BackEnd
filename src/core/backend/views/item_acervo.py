import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q

from core.backend.models import Item
from core.backend.serializers.item_acervo import ItemAcervoSerializer


class ItemAcervoFilter(django_filters.FilterSet):
    # Busca geral por texto
    busca_geral = django_filters.CharFilter(method="filter_busca_geral")

    def filter_busca_geral(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(
            Q(titulo__icontains=value)
            | Q(descricao__icontains=value)
            | Q(procedencia__icontains=value)
            | Q(datacao__icontains=value)
            | Q(observacoes_curadoria__icontains=value)
        ).distinct()

    class Meta:
        model = Item
        fields = {
            "titulo": ["exact", "icontains"],
            "colecao": ["exact"],
            "materia_prima": ["exact"],
            "subtipo": ["exact"],
            "localizacao_atual": ["exact"],
            "estado_conservacao": ["exact"],
            "inteireza": ["exact"],
            "categoria_acervo": ["exact"],
            "acervo": ["exact"],
            "procedencia": ["icontains"],
            "datacao": ["icontains"],
        }


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
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ItemAcervoFilter
    search_fields = ["titulo", "descricao", "procedencia", "datacao"]
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]  # Permite leitura pública, escrita apenas autenticada
