from django.db.models import *

class Tour(Model):
    
    name = CharField(
        'Имя тура',
        max_length=256
    )

    price = CharField(
        'Цена тура',
        max_length=128
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:

        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'