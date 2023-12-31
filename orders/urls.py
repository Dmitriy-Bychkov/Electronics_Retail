from django.urls import path
from orders.apps import OrdersConfig
from orders.views import OrderCreateAPIView, OrderListAPIView, \
    OrderRetrieveAPIView, OrderUpdateAPIView, OrderDestroyAPIView

app_name = OrdersConfig.name

urlpatterns = [
    path('create_order/', OrderCreateAPIView.as_view(),
         name='create_order'),
    path('', OrderListAPIView.as_view(),
         name='list_orders'),
    path('detail_order/<int:pk>/', OrderRetrieveAPIView.as_view(),
         name='detail_order'),
    path('update_order/<int:pk>/', OrderUpdateAPIView.as_view(),
         name='update_order'),
    path('delete_order/<int:pk>/', OrderDestroyAPIView.as_view(),
         name='delete_order'),
]
