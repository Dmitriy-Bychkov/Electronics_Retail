from rest_framework import serializers
from companies.models import Company
from companies.validators import company_create_validator


class CompanyCreateSerializer(serializers.ModelSerializer):
    """ Сериалайзер модели 'Компания' """

    class Meta:
        model = Company
        exclude = ('creation_date',)

        # Проверка на правильность заполнения полей у объекта - 'Компания'
        validators = [
            company_create_validator,
        ]


class CompanySerializer(serializers.ModelSerializer):
    """ Сериалайзер списка компаний """

    class Meta:
        model = Company
        fields = '__all__'


class CompanyUpdateSerializer(serializers.ModelSerializer):
    """ Сериалайзер изменения компании """

    class Meta:
        model = Company
        exclude = ('supplier_debt',)
