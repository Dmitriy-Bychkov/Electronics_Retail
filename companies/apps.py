from django.apps import AppConfig


class CompaniesConfig(AppConfig):
    """ Представление общего заголовка 'Компании' в админке """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'companies'
    verbose_name = 'компании и товары'
