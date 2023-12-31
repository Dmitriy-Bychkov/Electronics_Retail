from django.apps import AppConfig


class UsersConfig(AppConfig):
    """ Представление общего заголовка 'пользователи' в админке """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'пользователи'
