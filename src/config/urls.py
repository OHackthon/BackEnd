from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.backend.views import LocalizacaoViewSet, MateriaPrimaViewSet, ItemAcervoViewSet, ColecaoViewSet, ColecionadorViewSet, AcervoViewSet, CategoriaAcervoViewSet, ReservaViewSet
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from core.users.views import UserViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'localizacoes', LocalizacaoViewSet, basename='localizacoes')
router.register(r'materias-primas', MateriaPrimaViewSet, basename='materias-primas')
router.register(r'itens-acervo', ItemAcervoViewSet, basename='itens-acervo')
router.register(r'colecoes', ColecaoViewSet, basename='colecoes')
router.register(r'colecionadores', ColecionadorViewSet, basename='colecionadores')
router.register(r'acervos', AcervoViewSet, basename='acervos')
router.register(r'categorias-acervo', CategoriaAcervoViewSet, basename='categorias-acervo')
router.register(r'reservas', ReservaViewSet, basename='reservas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'api'), namespace='api')),
    
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/media/", include(uploader_router.urls)),
    
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)