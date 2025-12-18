from .categoriaAcervo import CategoriaAcervoViewSet
from .colecao import ColecaoViewSet
from .colecionador import ColecionadorViewSet
from .item import ItemViewSet
from .localizacao import LocalizacaoViewSet
from .materiaPrima import MateriaPrimaViewSet
from .reserva import ReservaViewSet
from .subTipo import SubtipoMaterialViewSet
from .user import UserViewSet

__all__ = [
    "CategoriaAcervoViewSet",
    "ColecaoViewSet",
    "ColecionadorViewSet",
    "ItemViewSet",
    "LocalizacaoViewSet",
    "MateriaPrimaViewSet",
    "ReservaViewSet",
    "SubtipoMaterialViewSet",
    "UserViewSet",
]
