from clients.models import Client
from rest_framework.serializers import *

class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'