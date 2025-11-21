from django.db import models 

from .materia_prima import MateriaPrima

class SubtipoMaterial(models.Model):
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE, related_name='subtipos')
    termo = models.CharField(max_length=100)

    class Meta:
        # Garante que não exista o mesmo termo repetido dentro da mesma matéria-prima
        unique_together = ('materia_prima', 'termo')

    def __str__(self):
        return f"{self.termo} ({self.materia_prima.nome})"