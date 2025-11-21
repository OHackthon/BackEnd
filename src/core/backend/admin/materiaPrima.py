from django.contrib.admin import ModelAdmin
from core.backend.models import MateriaPrima

@admin.register(MateriaPrima)
class AdminMateriaPrima(ModelAdmin):
    list_display = ("nome", "descricao", "fornecedor", "quantidade", "unidade_medida", "data_entrada")
    search_fields = ('nome', "descricao", "fornecedor__nome")
    ordering = ("-id",)
