from django.contrib.admin import ModelAdmin
from core.backend.models import Colecao

@admin.register(Colecao)
class AdminItemAcervo(ModelAdmin):
    list_display = ("titulo", "descricao", "colecao", "categoria", "localizacao", "data_aquisicao")
    search_fields = ('titulo', "descricao", "colecao__nome", "categoria__nome", "localizacao__endereco")
    ordering = ("-id",)