from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.backend.views import LocalizacaoViewSet, MateriaPrimaViewSet, ItemAcervoViewSet, ColecaoViewSet


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.users.views import UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'localizacao', LocalizacaoViewSet, basename='localizacao')
router.register(r'materiaprima', MateriaPrimaViewSet, basename='materiaprima')
router.register(r'itemacervo', ItemAcervoViewSet, basename='itemacervo')
router.register(r'usuario', ColecaoViewSet, basename='usuario')
router.register(r'colecao', ColecaoViewSet, basename='colecao')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'api'), namespace='api')),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]