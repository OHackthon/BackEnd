from django.db import models 
from .colecionador import Colecionador

class Colecao(models.Model):
    nome_colecao = models.CharField(max_length=100)
    colecionador = models.ForeignKey(Colecionador, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=255 null=True, blank=True)
    
    # 'auto_now_add' preenche a data automaticamente na criação
    data_registro_sistema = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nome_colecao