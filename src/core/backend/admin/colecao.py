from django.contrib import admin
from core.backend.models import Colecao


@admin.register(Colecao)
class AdminColecao(admin.ModelAdmin):
    list_display = (
        "nome_colecao",
        "nome_colecionador",
        "data_aquisicao",
        "data_registro_sistema",
    )
    search_fields = ("nome_colecao", "nome_colecionador", "descricao_origem")
    ordering = ("-id",)
