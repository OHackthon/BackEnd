from django.db import models


class MateriaPrima(models.Model):
    materia = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.materia
