from django.contrib import admin
from core.backend.models import MateriaPrima


@admin.register(MateriaPrima)
class AdminMateriaPrima(admin.ModelAdmin):
    list_display = ("materia",)
    search_fields = ("materia",)
    ordering = ("-id",)
