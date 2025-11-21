# core/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ["-date_joined"]
    list_display = ("email", "name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "name")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Informações pessoais"), {"fields": ("name",)}),
        (_("Permissões"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Datas importantes"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", "password1", "password2", "is_active", "is_staff", "is_superuser", "is_management"),
        }),
    )

    # Campo usado como identificador
    add_form_template = None
    filter_horizontal = ("groups", "user_permissions")