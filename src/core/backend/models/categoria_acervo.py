from django.db import models

class CategoriaAcervo(models.Model):
    nome_categoria = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome_categoria