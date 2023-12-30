from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from companies.models import Company
from companies.serializers import CompanyCreateSerializer, CompanySerializer, \
    CompanyUpdateSerializer
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
