from django.db import models
class Localizacao(models.Model):
    nome_local = models.CharField(max_length=100, unique=True)  
    capacidade_estimada = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    def _str_(self):
        return self.nome_local