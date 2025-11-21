from django.contrib.admin import ModelAdmin
from core.backend.models import categoriaAcervo

@admin.register(categoriaAcervo)
class AdminCategoriaAcervo(ModelAdmin):
    list_display = ("nome", "descricao")
    search_fields = ('nome', "descricao")
    ordering = ("-id",)