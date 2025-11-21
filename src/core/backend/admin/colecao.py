from django.contrib.admin import ModelAdmin
from core.backend.models import Colecao

@admin.register(Colecao)
class AdminColecao(ModelAdmin):
    list_display = ("nome", "descricao", "data_inicio", "data_fim")
    search_fields = ('nome', "descricao")
    ordering = ("-id",)