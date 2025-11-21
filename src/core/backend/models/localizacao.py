from django.db import models


class Localizacao(models.Model):
    nome_local = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.nome_local
