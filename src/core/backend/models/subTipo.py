from django.db import models 
from .materiaPrima import MateriaPrima
class SubtipoMaterial(models.Model):
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE, related_name='subtipos')
    termo = models.CharField(max_length=100)
    class Meta:
        unique_together = ('materia_prima', 'termo')
    def _str_(self):
        return f"{self.termo} ({self.materia_prima.termo})"