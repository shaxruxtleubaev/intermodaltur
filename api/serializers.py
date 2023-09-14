from rest_framework.serializers import *
from clients.models import Client
from tours.models import Tour

class ClientSerializer(ModelSerializer):

    class Meta:

        model = Client
        fields = '__all__'

class TourSerializer(ModelSerializer):

    class Meta:

        model = Tour
        fields = '__all__'