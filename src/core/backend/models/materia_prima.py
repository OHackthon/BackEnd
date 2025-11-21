from django.db import models

class MateriaPrima(models.Model):
    MATERIA_PRIMA = [
        ('ANIMAL', 'Animal'),
        ('VEGETAL', 'Vegetal'),
        ('MINERAL', 'Mineral'),
        ('OUTRO', 'Outro'),
    ]

    nome = models.CharField(max_length=50, choices=MATERIA_PRIMA)

    def _str_(self):
        return self.nome

