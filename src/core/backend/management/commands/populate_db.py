from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.backend.models import (
    CategoriaAcervo,
    Colecao,
    Item,
    Localizacao,
    MateriaPrima,
    SubtipoMaterial,
)
import random
from datetime import date


class Command(BaseCommand):
    help = "Popula o banco de dados com dados de teste"

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando população do banco de dados...")

        # Criar usuário admin se não existir
        user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@example.com",
                "is_staff": True,
                "is_superuser": True,
            },
        )
        if created:
            user.set_password("admin")
            user.save()
            self.stdout.write("Usuário admin criado.")
        else:
            self.stdout.write("Usuário admin já existe.")

        # Categorias
        categorias = ["Pintura", "Escultura", "Fotografia", "Mobiliário", "Numismática"]
        objs_categorias = []
        for cat in categorias:
            obj, _ = CategoriaAcervo.objects.get_or_create(
                nome_categoria=cat, defaults={"descricao": f"Categoria de {cat}"}
            )
            objs_categorias.append(obj)
        self.stdout.write(f"{len(objs_categorias)} categorias criadas/verificadas.")

        # Localizações
        locais = [
            "Reserva Técnica 1",
            "Sala de Exposição A",
            "Corredor Principal",
            "Armazém B",
        ]
        objs_locais = []
        for loc in locais:
            obj, _ = Localizacao.objects.get_or_create(
                nome_local=loc,
                defaults={
                    "capacidade_estimada": 100,
                    "estado": "SP",
                    "cidade": "São Paulo",
                },
            )
            objs_locais.append(obj)
        self.stdout.write(f"{len(objs_locais)} localizações criadas/verificadas.")

        # Matéria Prima
        materias = ["Madeira", "Metal", "Papel", "Tela", "Cerâmica"]
        objs_materias = []
        for mat in materias:
            obj, _ = MateriaPrima.objects.get_or_create(materia=mat)
            objs_materias.append(obj)
        self.stdout.write(f"{len(objs_materias)} matérias-primas criadas/verificadas.")

        # Subtipos
        subtipos_map = {
            "Madeira": ["Carvalho", "Pinho", "Mogno"],
            "Metal": ["Ferro", "Bronze", "Ouro"],
            "Papel": ["Papel Arroz", "Cartolina"],
            "Tela": ["Algodão", "Linho"],
            "Cerâmica": ["Barro", "Porcelana"],
        }
        objs_subtipos = []
        for mat_obj in objs_materias:
            termos = subtipos_map.get(mat_obj.materia, [])
            for termo in termos:
                obj, _ = SubtipoMaterial.objects.get_or_create(
                    materia_prima=mat_obj, termo=termo
                )
                objs_subtipos.append(obj)
        self.stdout.write(f"{len(objs_subtipos)} subtipos criados/verificados.")

        # Coleções
        colecoes = ["Coleção Moderna", "Coleção Clássica", "Doação Família Silva"]
        objs_colecoes = []
        for col in colecoes:
            obj, _ = Colecao.objects.get_or_create(
                nome_colecao=col,
                defaults={
                    "nome_colecionador": "João Silva",
                    "data_aquisicao": date(2020, 1, 1),
                    "descricao_origem": "Doação",
                },
            )
            objs_colecoes.append(obj)
        self.stdout.write(f"{len(objs_colecoes)} coleções criadas/verificadas.")

        # Itens
        for i in range(1, 21):  # Criar 20 itens
            numero_acervo = f"ACERVO-{i:04d}"
            if not Item.objects.filter(numero_acervo=numero_acervo).exists():
                materia = random.choice(objs_materias)
                # Filtrar subtipos da materia escolhida
                subtipos_da_materia = [
                    s for s in objs_subtipos if s.materia_prima == materia
                ]
                subtipo = (
                    random.choice(subtipos_da_materia) if subtipos_da_materia else None
                )

                Item.objects.create(
                    numero_acervo=numero_acervo,
                    titulo=f"Obra de Arte {i}",
                    colecao=random.choice(objs_colecoes),
                    materia_prima=materia,
                    subtipo=subtipo,
                    localizacao_atual=random.choice(objs_locais),
                    categoria_acervo=random.choice(objs_categorias),
                    estado_conservacao=random.choice(["BOM", "REGULAR", "FRAGMENTADO"]),
                    criado_por=user,
                    dimensoes="10x10x10",
                    peso=1.5,
                )
        self.stdout.write("Itens criados.")

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
