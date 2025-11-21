from django.db import models
from .item_acervo import Item
from .localizacao import Localizacao
from core.users.models import User


class Reserva(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.PROTECT, related_name="movimentacoes"
    )
    responsavel = models.ForeignKey(User, on_delete=models.PROTECT)

    local_origem = models.ForeignKey(
        Localizacao, on_delete=models.PROTECT, related_name="saidas"
    )
    local_destino = models.ForeignKey(
        Localizacao, on_delete=models.PROTECT, related_name="entradas"
    )

    data_movimentacao = models.DateTimeField(auto_now_add=True)

    TIPO_MOVIMENTO_CHOICES = [
        ("INTERNO", "Movimentação Interna"),
        ("SAIDA_EXTERNA", "Saída Externa / Empréstimo"),
    ]
    tipo_movimento = models.CharField(max_length=50, choices=TIPO_MOVIMENTO_CHOICES)

    def __str__(self):
        return f"Reserva do item {self.item} por {self.responsavel}"