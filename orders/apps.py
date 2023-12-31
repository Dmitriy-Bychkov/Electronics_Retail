from django.apps import AppConfig


class OrdersConfig(AppConfig):
    """ Представление общего заголовка 'Заказы' в админке """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    verbose_name = 'заказы'
