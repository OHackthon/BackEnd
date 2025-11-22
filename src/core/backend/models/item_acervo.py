from django.db import models 

from uploader.models import Image
from .colecao import Colecao
from .materia_prima import MateriaPrima
from .sub_tipo import SubtipoMaterial
from .localizacao import Localizacao
from .categoria_acervo import CategoriaAcervo
from .acervo import Acervo
from core.users.models import User

class Item(models.Model):
    acervo = models.ForeignKey(Acervo, on_delete=models.PROTECT)
    nome = models.CharField(max_length=200)
    imagem = models.ForeignKey(Image, related_name="+", on_delete=models.CASCADE, null=True, blank=True, default=None)
    colecao = models.ForeignKey(Colecao, on_delete=models.PROTECT)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.PROTECT)
    subtipo = models.ForeignKey(SubtipoMaterial, on_delete=models.SET_NULL, null=True, blank=True)
    localizacao_atual = models.ForeignKey(Localizacao, on_delete=models.PROTECT)
    categoria_acervo = models.ForeignKey(CategoriaAcervo, on_delete=models.PROTECT)
    procedencia = models.CharField(max_length=255, null=True, blank=True)
    datacao = models.CharField(max_length=100, null=True, blank=True)
    
    ESTADO_CHOICES = [
        ('BOM', 'Bom'),
        ('REGULAR', 'Regular'),
        ('FRAGMENTADO', 'Fragmentado'),
    ]
    INTEIREZA = [
        ('INTEIRO', 'Inteiro'),
        ('PARCIAL', 'Parcial'),
        ('FRAGMENTADO', 'Fragmentado'),
    ]
    estado_conservacao = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    dimensoes = models.CharField(max_length=100, null=True, blank=True)
    peso_g = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    inteireza = models.CharField(max_length=50, choices=INTEIREZA)
    observacoes_curadoria = models.TextField(null=True, blank=True)

    # Auditoria de Criação
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name='itens_criados')
    data_registro = models.DateTimeField(auto_now_add=True) # Data fixa da criação
    ultima_atualizacao = models.DateTimeField(auto_now=True) # Atualiza sempre que salvar

    def __str__(self):
        return f"{self.acervo} - {self.nome}"