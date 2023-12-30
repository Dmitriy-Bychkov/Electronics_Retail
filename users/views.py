from rest_framework import generics
from users.models import User
from users.permissions import IsActiveUser
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Создание пользователя """

    serializer_class = UserSerializer
    permission_classes = [IsActiveUser]


class UserListAPIView(generics.ListAPIView):
    """ Вывод списка пользователей """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsActiveUser]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одного пользователя """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsActiveUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование пользователя """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsActiveUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """

    queryset = User.objects.all()
    permission_classes = [IsActiveUser]
