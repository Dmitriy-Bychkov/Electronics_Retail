import os
from dotenv import load_dotenv
from config.settings import BASE_DIR
from django.core.management import BaseCommand
from users.models import User

env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)


class Command(BaseCommand):
    """ Класс для создания (переопределения) суперюзера """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.com',
            first_name='Admin',
            last_name='Dmitriy',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password(os.getenv('SUPERUSER_PASSWORD'))
        user.save()
