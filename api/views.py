from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from .serializers import (
    ClientSerializer,
    TourSerializer
)
from clients.models import Client
from tours.models import Tour

class ClientAPIView(APIView):

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
class TourAPIView(APIView):

    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )