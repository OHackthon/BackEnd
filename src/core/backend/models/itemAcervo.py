from django.db import models
from django.contrib.auth.models import User
from .colecao import Colecao
from .materiaPrima import MateriaPrima
from .subTipo import SubtipoMaterial
from .localizacao import Localizacao
from .categoriaAcervo import CategoriaAcervo
class Item(models.Model):
    numero_acervo = models.CharField(max_length=50, unique=True)
    titulo = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to="itens/")
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.PROTECT)
    subtipo = models.ForeignKey(
        SubtipoMaterial, on_delete=models.SET_NULL, null=True, blank=True
    )
    localizacao_atual = models.ForeignKey(Localizacao, on_delete=models.PROTECT)
    categoria_acervo = models.ForeignKey(CategoriaAcervo, on_delete=models.PROTECT)
    procedencia = models.CharField(max_length=255, null=True, blank=True)
    datacao_estimada = models.CharField(max_length=100, null=True, blank=True)
    ESTADO_CHOICES = [
        ("BOM", "Bom"),
        ("REGULAR", "Regular"),
        ("FRAGMENTADO", "Fragmentado"),
    ]
    INTEREZA = [
        ("INTEIRO", "Inteiro"),
        ("PARCIAL", "Parcial"),
        ("FRAGMENTADO", "Fragmentado"),
    ]
    estado_conservacao = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    inteireza = models.CharField(max_length=50, choices=INTEREZA, null=True, blank=True)
    dimensoes = models.CharField(max_length=100, null=True, blank=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    descricao_detalhada = models.TextField(null=True, blank=True)
    observacoes_curadoria = models.TextField(null=True, blank=True)
    criado_por = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="itens_criados"
    )
    data_registro = models.DateTimeField(auto_now_add=True)  
    ultima_atualizacao = models.DateTimeField(
        auto_now=True
    )  
    def _str_(self):
        return f"{self.numero_acervo} - {self.titulo}"