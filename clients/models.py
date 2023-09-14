from django.db.models import *

class Client(Model):

    fullname = CharField(
        'ФИО',
        max_length=128
    )

    date_of_birth = DateField(
        'Дата рождения',
        max_length=128
    )

    country = CharField(
        'Страна',
        max_length=128
    )

    passport_data = CharField(
        'Серия и номер паспорта',
        max_length=128
    )

    phone_number = CharField(
        'Телефон номер',
        max_length=128
    )

    def __str__(self):
        return f'{self.fullname}'
    
    class Meta:

        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'