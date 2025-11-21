from django.contrib import admin
from core.backend.models import CategoriaAcervo


@admin.register(CategoriaAcervo)
class AdminCategoriaAcervo(admin.ModelAdmin):
    list_display = ("nome_categoria", "descricao")
    search_fields = ("nome_categoria", "descricao")
    ordering = ("-id",)
