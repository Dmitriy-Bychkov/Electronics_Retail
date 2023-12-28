from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Представление пользователей в админке """

    list_display = (
        'first_name',
        'last_name',
        'email',
    )
    search_fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'country',
    )
