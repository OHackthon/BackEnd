from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
import pandas as pd
from django.contrib.auth.models import User
from core.backend.models import (
    CategoriaAcervo,
    Colecao,
    Item,
    Localizacao,
    MateriaPrima,
    SubtipoMaterial,
    Reserva,
)
from core.backend.serializers.categoriaAcervo import CategoriaAcervoSerializer
from core.backend.serializers.colecao import ColecaoSerializer
from core.backend.serializers.ItemAcervo import ItemSerializer
from core.backend.serializers.localizacao import LocalizacaoSerializer
from core.backend.serializers.materiaprima import MateriaPrimaSerializer
from core.backend.serializers.subTipo import SubtipoMaterialSerializer
from core.backend.serializers.user import UserSerializer
from core.backend.serializers.reserva import ReservaSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class CategoriaAcervoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaAcervo.objects.all()
    serializer_class = CategoriaAcervoSerializer


class ColecaoViewSet(viewsets.ModelViewSet):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    pagination_class = None


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=False, methods=["post"])
    def upload_excel(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response(
                {"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            df = pd.read_excel(file)
            created_count = 0
            errors = []

            for index, row in df.iterrows():
                try:
                    # Mandatory fields
                    numero_acervo = str(row.get("numero_acervo", ""))
                    titulo = row.get("titulo", "")

                    if not numero_acervo or not titulo:
                        errors.append(f"Row {index}: Missing numero_acervo or titulo")
                        continue

                    # Check if item already exists
                    if Item.objects.filter(numero_acervo=numero_acervo).exists():
                        errors.append(
                            f"Row {index}: Item {numero_acervo} already exists"
                        )
                        continue

                    # FKs - Get or Create
                    colecao_name = row.get("colecao")
                    if not colecao_name:
                        errors.append(f"Row {index}: Missing colecao")
                        continue
                    colecao, _ = Colecao.objects.get_or_create(
                        nome_colecao=colecao_name
                    )

                    materia_name = row.get("materia_prima")
                    if not materia_name:
                        errors.append(f"Row {index}: Missing materia_prima")
                        continue
                    materia, _ = MateriaPrima.objects.get_or_create(
                        materia=materia_name
                    )

                    subtipo_name = row.get("subtipo")
                    subtipo = None
                    if subtipo_name:
                        subtipo, _ = SubtipoMaterial.objects.get_or_create(
                            termo=subtipo_name, materia_prima=materia
                        )

                    local_name = row.get("localizacao")
                    if not local_name:
                        errors.append(f"Row {index}: Missing localizacao")
                        continue
                    local, _ = Localizacao.objects.get_or_create(nome_local=local_name)

                    cat_name = row.get("categoria")
                    if not cat_name:
                        errors.append(f"Row {index}: Missing categoria")
                        continue
                    categoria, _ = CategoriaAcervo.objects.get_or_create(
                        nome_categoria=cat_name
                    )

                    # Create Item
                    Item.objects.create(
                        numero_acervo=numero_acervo,
                        titulo=titulo,
                        colecao=colecao,
                        materia_prima=materia,
                        subtipo=subtipo,
                        localizacao_atual=local,
                        categoria_acervo=categoria,
                        estado_conservacao=row.get("estado_conservacao", "REGULAR"),
                        inteireza=row.get("inteireza", "INTEIRO"),
                        descricao_detalhada=row.get("descricao", ""),
                        criado_por=request.user,
                    )
                    created_count += 1
                except Exception as e:
                    errors.append(f"Row {index}: {str(e)}")

            return Response(
                {
                    "message": f"{created_count} items created successfully",
                    "errors": errors,
                },
                status=status.HTTP_200_OK,
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer


class MateriaPrimaViewSet(viewsets.ModelViewSet):
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer


class SubtipoMaterialViewSet(viewsets.ModelViewSet):
    queryset = SubtipoMaterial.objects.all()
    serializer_class = SubtipoMaterialSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
