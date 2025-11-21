from django.contrib.admin import ModelAdmin
from core.backend.models import Localizacao

@admin.register(Localizacao)
class AdminLocalizacao(ModelAdmin):
    list_display = ("endereco", "cidade", "estado", "pais")
    search_fields = ('endereco', 'cidade', 'estado', 'pais')
    ordering = ("-id",)