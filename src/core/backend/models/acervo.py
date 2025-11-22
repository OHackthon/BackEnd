from django.db import models

class Acervo(models.Model):
    numero_acervo = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.numero_acervo