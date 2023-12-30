from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериалайзер модели User """

    class Meta:
        model = User
        fields = '__all__'
