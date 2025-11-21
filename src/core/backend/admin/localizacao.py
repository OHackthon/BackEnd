from django.contrib import admin
from core.backend.models import Localizacao


@admin.register(Localizacao)
class AdminLocalizacao(admin.ModelAdmin):
    list_display = ("nome_local", "cidade", "estado", "capacidade_estimada")
    search_fields = ("nome_local", "cidade", "estado", "bairro", "rua")
    ordering = ("-id",)
