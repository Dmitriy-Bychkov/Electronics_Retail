from rest_framework.serializers import ValidationError


def company_create_validator(value):
    """ Проверка на правильность заполнения полей у объекта - 'Компания' """

    try:
        if value['type'] == 'завод':
            if value['supplier']:
                raise ValidationError('У завода нет поставщиков!')
    except KeyError:
        pass
