from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from companies.models import Company, Product
from companies.serializers import CompanyCreateSerializer, CompanySerializer, \
    CompanyUpdateSerializer, ProductSerializer
from users.permissions import IsActiveUser


class CompanyCreateAPIView(generics.CreateAPIView):
    """ Создание компании """

    serializer_class = CompanyCreateSerializer
    permission_classes = [IsActiveUser]

    def perform_create(self, serializer):
        """ Переопределяем метод создания нового объекта """

        new_company = serializer.save()
        new_company.save()


class CompanyListAPIView(generics.ListAPIView):
    """ Вывод списка компаний """

    serializer_class = CompanySerializer
    permission_classes = [IsActiveUser]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('country',)
    ordering_fields = ['country']

    def get_queryset(self):
        """ Определяем 'queryset' для вывода объектов """

        queryset = Company.objects.all()
        return queryset


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр подробной информации о компании """

    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [IsActiveUser]


class CompanyUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование компании """

    serializer_class = CompanyUpdateSerializer
    queryset = Company.objects.all()
    permission_classes = [IsActiveUser]


class CompanyDestroyAPIView(generics.DestroyAPIView):
    """ Удаление компании """

    queryset = Company.objects.all()
    permission_classes = [IsActiveUser]


class ProductCreateAPIView(generics.CreateAPIView):
    """ Создание нового товара """

    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]

    def perform_create(self, serializer):
        """ Переопределяем метод создания нового объекта """

        new_product = serializer.save()
        new_product.save()


class ProductListAPIView(generics.ListAPIView):
    """ Вывод списка всех товаров """

    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]

    def get_queryset(self):
        """ Переопределяем метод вывода объектов """

        queryset = Product.objects.all()
        return queryset


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр подробной информации о товаре """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование товара """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """ Удаление товара """

    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]
