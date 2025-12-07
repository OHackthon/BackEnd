import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from core.backend.models import (
    Item,
    Colecao,
    MateriaPrima,
    SubtipoMaterial,
    Localizacao,
    CategoriaAcervo,
)
class Command(BaseCommand):
    help = "Seeds the database with initial data and real photos"
    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin")
            self.stdout.write('Superuser "admin" created.')
        user = User.objects.get(username="admin")
        colecoes = [
            {
                "nome": "Coleção Arqueológica Sambaqui",
                "desc": "Artefatos encontrados nos sambaquis da região.",
            },
            {
                "nome": "Coleção Etnográfica Indígena",
                "desc": "Objetos de uso cotidiano e ritual de povos indígenas.",
            },
            {
                "nome": "Coleção Histórica Regional",
                "desc": "Peças do período colonial e imperial da região.",
            },
        ]
        db_colecoes = {}
        for col in colecoes:
            c, _ = Colecao.objects.get_or_create(
                nome_colecao=col["nome"], defaults={"descricao_origem": col["desc"]}
            )
            db_colecoes[col["nome"]] = c
        materias = ["Pedra", "Cerâmica", "Osso", "Concha", "Madeira", "Metal"]
        db_materias = {}
        for mat in materias:
            m, _ = MateriaPrima.objects.get_or_create(materia=mat)
            db_materias[mat] = m
        subtipos = {
            "Pedra": ["Polida", "Lascada"],
            "Cerâmica": ["Simples", "Decorada"],
            "Osso": ["Trabalhado"],
            "Concha": ["Perfurada"],
        }
        db_subtipos = {}
        for mat_name, subs in subtipos.items():
            m = db_materias[mat_name]
            for sub in subs:
                s, _ = SubtipoMaterial.objects.get_or_create(termo=sub, materia_prima=m)
                db_subtipos[f"{sub} ({mat_name})"] = s
        locais = [
            "Reserva Técnica 1",
            "Exposição Permanente",
            "Laboratório de Restauro",
        ]
        db_locais = {}
        for loc in locais:
            l, _ = Localizacao.objects.get_or_create(nome_local=loc)
            db_locais[loc] = l
        categorias = ["Utensílio", "Adorno", "Arma", "Ritualístico"]
        db_categorias = {}
        for cat in categorias:
            c, _ = CategoriaAcervo.objects.get_or_create(nome_categoria=cat)
            db_categorias[cat] = c
        items_data = [
            {
                "numero": "ARQ-001",
                "titulo": "Machado de Pedra Polida",
                "colecao": "Coleção Arqueológica Sambaqui",
                "materia": "Pedra",
                "subtipo": "Polida",
                "local": "Exposição Permanente",
                "categoria": "Arma",
                "estado": "BOM",
                "inteireza": "INTEIRO",
                "img_url": "https://images.unsplash.com/photo-1599940824399-b87987ce0799?q=80&w=800&auto=format&fit=crop",  
                "desc": "Lâmina de machado em diabásio polido, fio cortante preservado.",
                "dimensoes": "12 x 5 x 3 cm",
                "datacao": "1000 - 1200 DC",
                "procedencia": "Sambaqui do Rio Comprido",
            },
            {
                "numero": "ARQ-002",
                "titulo": "Vaso Cerâmico Decorado",
                "colecao": "Coleção Etnográfica Indígena",
                "materia": "Cerâmica",
                "subtipo": "Decorada",
                "local": "Reserva Técnica 1",
                "categoria": "Utensílio",
                "estado": "REGULAR",
                "inteireza": "PARCIAL",
                "img_url": "https://images.unsplash.com/photo-1610701596007-11502861dcfa?q=80&w=800&auto=format&fit=crop",  
                "desc": "Fragmento de borda de vasilha cerâmica com incisões geométricas.",
                "dimensoes": "25cm (diâmetro) x 15cm (altura)",
                "datacao": "800 - 1000 DC",
                "procedencia": "Sítio Arqueológico Enseada",
            },
            {
                "numero": "ARQ-003",
                "titulo": "Ponta de Flecha",
                "colecao": "Coleção Arqueológica Sambaqui",
                "materia": "Pedra",
                "subtipo": "Lascada",
                "local": "Exposição Permanente",
                "categoria": "Arma",
                "estado": "BOM",
                "inteireza": "INTEIRO",
                "img_url": "https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?q=80&w=800&auto=format&fit=crop",  
                "desc": "Ponta de projétil bifacial em quartzo hialino.",
                "dimensoes": "4 x 2 x 0.5 cm",
                "datacao": "1500 - 500 AC",
                "procedencia": "Sambaqui Morro do Ouro",
            },
            {
                "numero": "ARQ-004",
                "titulo": "Colar de Conchas",
                "colecao": "Coleção Arqueológica Sambaqui",
                "materia": "Concha",
                "subtipo": "Perfurada",
                "local": "Exposição Permanente",
                "categoria": "Adorno",
                "estado": "BOM",
                "inteireza": "INTEIRO",
                "img_url": "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?q=80&w=800&auto=format&fit=crop",  
                "desc": "Contas de colar feitas de conchas marinhas perfuradas.",
                "dimensoes": "45 cm (comprimento)",
                "datacao": "Indeterminada",
                "procedencia": "Doação Particular",
            },
            {
                "numero": "ARQ-005",
                "titulo": "Morteiro de Pedra",
                "colecao": "Coleção Arqueológica Sambaqui",
                "materia": "Pedra",
                "subtipo": "Polida",
                "local": "Reserva Técnica 1",
                "categoria": "Utensílio",
                "estado": "BOM",
                "inteireza": "INTEIRO",
                "img_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=800&auto=format&fit=crop",  
                "desc": "Morteiro utilizado para moagem de pigmentos e alimentos.",
                "dimensoes": "30 x 30 x 10 cm",
                "datacao": "2000 AC",
                "procedencia": "Sambaqui Cubatão",
            },
            {
                "numero": "ARQ-006",
                "titulo": "Estatueta Antropomorfa",
                "colecao": "Coleção Etnográfica Indígena",
                "materia": "Cerâmica",
                "subtipo": "Decorada",
                "local": "Exposição Permanente",
                "categoria": "Ritualístico",
                "estado": "FRAGMENTADO",
                "inteireza": "FRAGMENTADO",
                "img_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=800&auto=format&fit=crop",  
                "desc": "Representação antropomorfa estilizada.",
                "dimensoes": "15 x 8 x 5 cm",
                "datacao": "1200 DC",
                "procedencia": "Escavação 1995 - Setor B",
            },
        ]
        for item_data in items_data:
            if Item.objects.filter(numero_acervo=item_data["numero"]).exists():
                continue
            self.stdout.write(f"Creating item {item_data['titulo']}...")
            try:
                response = requests.get(item_data["img_url"])
                if response.status_code == 200:
                    item = Item(
                        numero_acervo=item_data["numero"],
                        titulo=item_data["titulo"],
                        colecao=db_colecoes[item_data["colecao"]],
                        materia_prima=db_materias[item_data["materia"]],
                        subtipo=db_subtipos.get(
                            f"{item_data['subtipo']} ({item_data['materia']})"
                        ),
                        localizacao_atual=db_locais[item_data["local"]],
                        categoria_acervo=db_categorias[item_data["categoria"]],
                        estado_conservacao=item_data["estado"],
                        inteireza=item_data["inteireza"],
                        descricao_detalhada=item_data["desc"],
                        dimensoes=item_data.get("dimensoes"),
                        datacao_estimada=item_data.get("datacao"),
                        procedencia=item_data.get("procedencia"),
                        criado_por=user,
                    )
                    file_name = f"{item_data['numero']}.jpg"
                    item.imagem.save(
                        file_name, ContentFile(response.content), save=True
                    )
                    self.stdout.write(f"Successfully created {item_data['titulo']}")
                else:
                    self.stdout.write(
                        self.style.ERROR(
                            f"Failed to download image for {item_data['titulo']}"
                        )
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error creating {item_data['titulo']}: {str(e)}")
                )
        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))