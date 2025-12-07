# from django.contrib import admin
# from core.backend.models import ModelExemplo

# # O @admin.register é um decorador fornecido pelo Django que
# # serve para registrar um Model no Django Admin, associando
# # esse model com uma classe de configuração

# @admin.register(ModelExemplo)
# # ModelAdmin é uma classe base do Django usada para configurar
# # como um model será exibido e controlado dentro do Django Admin.
# class AdminModelExemplo(admin.ModelAdmin):
#     list_display = ("nome", "ativo", "criado_em", "atualizado_em")
#     search_fields = ('nome', "descricao",)
#     ordering = ("-id",)
