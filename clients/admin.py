from django.contrib.admin import *
from .models import Client

@register(Client)
class ClientAdmin(ModelAdmin):

    list_display = ('id', 'fullname', 'phone_number')
    list_display_links = ('id', 'fullname', 'phone_number')
    ordering = ('-id',)