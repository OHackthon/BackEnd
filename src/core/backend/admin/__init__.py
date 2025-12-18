from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from core.backend.models import (
    CategoriaAcervo,
    Colecao,
    Colecionador,
    Item,
    Localizacao,
    MateriaPrima,
    Reserva,
    SubtipoMaterial,
)


@admin.register(CategoriaAcervo)
class CategoriaAcervoAdmin(admin.ModelAdmin):
    list_display = ("nome_categoria", "descricao")
    search_fields = ("nome_categoria",)


@admin.register(Colecao)
class ColecaoAdmin(admin.ModelAdmin):
    list_display = ("nome_colecao", "nome_colecionador")
    search_fields = ("nome_colecao",)


@admin.register(Colecionador)
class ColecionadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "data_registro_sistema")
    search_fields = ("nome", "email")
    list_filter = ("data_registro_sistema",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("numero_acervo", "titulo", "colecao")
    search_fields = ("numero_acervo", "titulo")
    list_filter = ("colecao", "estado_conservacao")


@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ("nome_local", "cidade")
    search_fields = ("nome_local",)


@admin.register(MateriaPrima)
class MateriaPrimaAdmin(admin.ModelAdmin):
    list_display = ("materia",)
    search_fields = ("materia",)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("item", "tipo_movimento", "data_movimentacao")
    search_fields = ("item__titulo",)
    list_filter = ("tipo_movimento", "data_movimentacao")


@admin.register(SubtipoMaterial)
class SubtipoMaterialAdmin(admin.ModelAdmin):
    list_display = ("termo", "materia_prima")
    search_fields = ("termo",)
    list_filter = ("materia_prima",)


# Unregister default User admin and register customized version
admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(DjangoUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email")
