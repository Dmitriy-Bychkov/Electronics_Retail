from django.db import models
from django.utils import timezone

from users.models import NULLABLE


class Product(models.Model):
    """ Модель продукта """

    name = models.CharField(max_length=200, verbose_name='название')
    model = models.CharField(max_length=200, verbose_name='модель')
    release_date = models.DateTimeField(default=timezone.now,
                                        verbose_name='дата релиза продукта')

    def __str__(self):
        """ Строковое отображение объекта """

        return f'{self.name}'

    class Meta:
        """ Представление написания заголовков в админке """

        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)


class Company(models.Model):
    """ Модель компании """

    class CompanyType(models.TextChoices):
        """ Класс для создания выбора типа компании """

        factory = 'завод'
        retail_network = 'розничная сеть'
        entrepreneur = 'индивидуальный предприниматель'

    name = models.CharField(max_length=150, verbose_name='название')
    email = models.EmailField(verbose_name='почта')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    building = models.CharField(max_length=20, verbose_name='дом')
    type = models.CharField(max_length=30, choices=CompanyType.choices,
                            verbose_name='тип компании')
    products = models.ManyToManyField(Product, verbose_name='товары')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE,
                                 verbose_name='поставщик')
    supplier_debt = models.DecimalField(max_digits=10, decimal_places=2,
                                        **NULLABLE,
                                        verbose_name='долг поставщику')
    creation_date = models.DateTimeField(default=timezone.now,
                                         verbose_name='дата и время создания')

    def __str__(self):
        """ Строковое отображение объекта """

        return f'{self.name}'

    class Meta:
        """ Представление написания заголовков в админке """

        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ('name',)
