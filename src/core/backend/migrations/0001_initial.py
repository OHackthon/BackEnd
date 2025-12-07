import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name='CategoriaAcervo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Colecao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_colecao', models.CharField(max_length=100)),
                ('nome_colecionador', models.CharField(blank=True, max_length=100, null=True)),
                ('data_aquisicao', models.DateField(blank=True, null=True)),
                ('descricao_origem', models.TextField(blank=True, null=True)),
                ('data_registro_sistema', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_local', models.CharField(max_length=100, unique=True)),
                ('capacidade_estimada', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('rua', models.CharField(blank=True, max_length=100, null=True)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_acervo', models.CharField(max_length=50, unique=True)),
                ('titulo', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='itens/')),
                ('procedencia', models.CharField(blank=True, max_length=255, null=True)),
                ('datacao_estimada', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_conservacao', models.CharField(choices=[('BOM', 'Bom'), ('REGULAR', 'Regular'), ('FRAGMENTADO', 'Fragmentado')], max_length=50)),
                ('inteireza', models.CharField(blank=True, choices=[('INTEIRO', 'Inteiro'), ('PARCIAL', 'Parcial'), ('FRAGMENTADO', 'Fragmentado')], max_length=50, null=True)),
                ('dimensoes', models.CharField(blank=True, max_length=100, null=True)),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('descricao_detalhada', models.TextField(blank=True, null=True)),
                ('observacoes_curadoria', models.TextField(blank=True, null=True)),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('categoria_acervo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.categoriaacervo')),
                ('colecao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.colecao')),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itens_criados', to=settings.AUTH_USER_MODEL)),
                ('localizacao_atual', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.localizacao')),
                ('materia_prima', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.materiaprima')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_movimentacao', models.DateTimeField(auto_now_add=True)),
                ('tipo_movimento', models.CharField(choices=[('INTERNO', 'Movimentação interna'), ('EXTERNA', 'Saída externa / Empréstimo')], max_length=20)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservas', to='backend.item')),
                ('local_destino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservas_destino', to='backend.localizacao')),
                ('local_origem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservas_origem', to='backend.localizacao')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubtipoMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termo', models.CharField(max_length=100)),
                ('materia_prima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtipos', to='backend.materiaprima')),
            ],
            options={
                'unique_together': {('materia_prima', 'termo')},
            },
        ),
        migrations.AddField(
            model_name='item',
            name='subtipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.subtipomaterial'),
        ),
    ]