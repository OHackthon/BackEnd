from django.db import models

class Colecionador(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    contato = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome