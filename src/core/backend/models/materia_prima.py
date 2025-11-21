from django.db import models

class MateriaPrima(models.Model):
    materia = models.CharField(max_length=50, unique=True)

    def _str_(self):
        return self.materia

