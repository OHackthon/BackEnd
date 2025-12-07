from django.db import models 
class Colecao(models.Model):
    nome_colecao = models.CharField(max_length=100)
    nome_colecionador = models.CharField(max_length=100, null=True, blank=True)
    data_aquisicao = models.DateField(null=True, blank=True)
    descricao_origem = models.TextField(null=True, blank=True)
    data_registro_sistema = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.nome_colecao