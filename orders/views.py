from rest_framework import generics
from orders.models import Order
from orders.serializers import OrderSerializer
from users.permissions import IsActiveUser


class OrderCreateAPIView(generics.CreateAPIView):
    """ Создание нового заказа """

    serializer_class = OrderSerializer
    permission_classes = [IsActiveUser]

    def perform_create(self, serializer):
        """ Переопределяем метод создания нового объекта """

        new_order = serializer.save()
        new_order.save()


class OrderListAPIView(generics.ListAPIView):
    """ Вывод списка всех заказов """

    serializer_class = OrderSerializer
    permission_classes = [IsActiveUser]

    def get_queryset(self):
        """ Переопределяем метод вывода объектов """

        queryset = Order.objects.all()
        return queryset


class OrderRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр подробной информации о заказе """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsActiveUser]


class OrderUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование заказа """

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsActiveUser]


class OrderDestroyAPIView(generics.DestroyAPIView):
    """ Удаление заказа """

    queryset = Order.objects.all()
    permission_classes = [IsActiveUser]
