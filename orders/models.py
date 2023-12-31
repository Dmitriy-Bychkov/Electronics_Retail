from django.db import models
from django.utils import timezone
from companies.models import Company, Product


class Order(models.Model):
    """ Модель заказа """

    supplier = models.ForeignKey(Company, on_delete=models.CASCADE,
                                 verbose_name='поставщик')
    products = models.ManyToManyField(Product, through='OrderProduct',
                                      verbose_name='продукты')
    order_date = models.DateTimeField(default=timezone.now,
                                      verbose_name='дата заказа')

    def __str__(self):
        """ Строковое отображение объекта """

        return f'Заказ {self.id} - {self.products}'

    class Meta:
        """ Представление написания заголовков в админке """

        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-order_date',)


class OrderProduct(models.Model):
    """ Промежуточная модель для связи Order и Product """

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='продукт')
    quantity = models.PositiveIntegerField(verbose_name='количество продукта')

    def __str__(self):
        """ Строковое отображение объекта """

        return f'Заказ {self.order.id} - {self.product}'

    class Meta:
        """ Представление написания заголовков в админке """

        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'
