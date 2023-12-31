import os
from dotenv import load_dotenv
from config.settings import BASE_DIR
from django.core.management import BaseCommand
from users.models import User

env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)


class Command(BaseCommand):
    """ Класс для создания обычного пользователя """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='user@user.com',
            first_name='User',
            last_name='User_Userovich',
            is_staff=False,
            is_superuser=False,
            is_active=False
        )

        user.set_password(os.getenv('USER_PASSWORD'))
        user.save()
