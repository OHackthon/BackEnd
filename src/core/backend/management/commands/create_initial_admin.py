import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Cria um superusuário inicial seguro se nenhum existir"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            default=os.environ.get("ADMIN_USERNAME", "admin"),
            help="Nome de usuário do admin",
        )
        parser.add_argument(
            "--email",
            default=os.environ.get("ADMIN_EMAIL", "admin@example.com"),
            help="Email do admin",
        )
        parser.add_argument(
            "--password",
            default=os.environ.get("ADMIN_PASSWORD"),
            help="Senha do admin (se não fornecida, será gerada)",
        )

    def handle(self, *args, **options):
        User = get_user_model()

        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(
                self.style.WARNING(
                    "Já existe um superusuário no sistema. Nenhuma ação realizada."
                )
            )
            return

        username = options["username"]
        email = options["email"]
        password = options["password"]

        if not password:
            password = get_random_string(12)
            generated = True
        else:
            generated = False

        try:
            User.objects.create_superuser(
                username=username, email=email, password=password
            )

            self.stdout.write(
                self.style.SUCCESS(f'Superusuário "{username}" criado com sucesso!')
            )
            if generated:
                self.stdout.write(
                    self.style.SUCCESS(f"Senha gerada automaticamente: {password}")
                )
                self.stdout.write(
                    self.style.WARNING(
                        "POR FAVOR, GUARDE ESTA SENHA EM UM LOCAL SEGURO."
                    )
                )

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro ao criar superusuário: {str(e)}"))
