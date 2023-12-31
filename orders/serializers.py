from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Заказов """

    class Meta:
        model = Order
        fields = '__all__'
