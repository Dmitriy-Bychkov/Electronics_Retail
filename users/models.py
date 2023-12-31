from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель для пользователей сервиса """

    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', default='no_image.jpg',
                               verbose_name='аватар', **NULLABLE)
    phone = models.CharField(unique=True, max_length=20, verbose_name='телефон',
                             **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=False,
                                    verbose_name='статус активности')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        """ Строковое отображение объекта """

        return f'{self.first_name} - {self.email}'

    class Meta:
        """ Представление написания заголовков в админке """

        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
