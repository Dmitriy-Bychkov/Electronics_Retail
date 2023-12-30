from django.contrib import admin
from companies.models import Company, Product


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ Представление компаний в админке """

    list_display = ('name', 'city', 'type', 'supplier_debt')
    list_filter = ('city',)
    actions = ['nullify_debt']

    def nullify_debt(self, request, queryset):
        """ Метод для обнуления задолженности перед поставщиком """

        for item in queryset:
            item.supplier_debt = 0
            item.save()
        self.message_user(request, 'Задолженность перед поставщиком обнулена')

    nullify_debt.short_description = 'Обнулить задолженность'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Представление продуктов в админке """

    list_display = ('name', 'model', 'release_date')
    list_filter = ('name',)
