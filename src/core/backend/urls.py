from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.backend.views.viewsets import (
    CategoriaAcervoViewSet,
    ColecaoViewSet,
    ItemViewSet,
    LocalizacaoViewSet,
    MateriaPrimaViewSet,
    SubtipoMaterialViewSet,
    UserViewSet,
    ReservaViewSet,
)
router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"categorias-acervo", CategoriaAcervoViewSet)
router.register(r"colecoes", ColecaoViewSet)
router.register(r"itens-acervo", ItemViewSet)
router.register(r"localizacoes", LocalizacaoViewSet)
router.register(r"materias-primas", MateriaPrimaViewSet)
router.register(r"subtipos", SubtipoMaterialViewSet)
router.register(r"reservas", ReservaViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]