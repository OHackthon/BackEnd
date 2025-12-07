from django.db import models
from django.contrib.auth.models import User
from .itemAcervo import Item
from .localizacao import Localizacao


class Reserva(models.Model):
    TIPO_MOVIMENTO_CHOICES = [
        ("INTERNO", "Movimentação interna"),
        ("EXTERNA", "Saída externa / Empréstimo"),
    ]

    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name="reservas")
    responsavel = models.ForeignKey(User, on_delete=models.PROTECT)
    local_origem = models.ForeignKey(
        Localizacao, on_delete=models.PROTECT, related_name="reservas_origem"
    )
    local_destino = models.ForeignKey(
        Localizacao, on_delete=models.PROTECT, related_name="reservas_destino"
    )
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    tipo_movimento = models.CharField(max_length=20, choices=TIPO_MOVIMENTO_CHOICES)

    def __str__(self):
        return f"{self.item.titulo} - {self.tipo_movimento}"
