from django.contrib import admin
from orders.models import Order, OrderProduct


class OrderProductInlineAdmin(admin.TabularInline):
    """ Представление инлайн заказовв админке через промежуочную таблицу """

    fields = ('order', 'product', 'quantity')
    extra = 1
    model = OrderProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Представление заказов в админке с
    инлайн связью с заказамии-продуктам
    """

    list_display = ('supplier', 'order_date',)
    list_filter = ('order_date',)
    inlines = [OrderProductInlineAdmin]
