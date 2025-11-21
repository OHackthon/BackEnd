from django.contrib import admin
from core.backend.models import Item


@admin.register(Item)
class AdminItemAcervo(admin.ModelAdmin):
    list_display = (
        "numero_acervo",
        "titulo",
        "colecao",
        "categoria_acervo",
        "localizacao_atual",
        "data_registro",
    )
    search_fields = (
        "numero_acervo",
        "titulo",
        "colecao__nome",
        "categoria_acervo__nome",
        "localizacao_atual__nome",
    )
    ordering = ("-id",)
