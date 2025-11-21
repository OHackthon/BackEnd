from django.contrib import admin
from core.backend.models import SubtipoMaterial


@admin.register(SubtipoMaterial)
class AdminSubTipo(admin.ModelAdmin):
    list_display = ("termo", "materia_prima")
    search_fields = ("termo", "materia_prima__materia")
    ordering = ("-id",)
