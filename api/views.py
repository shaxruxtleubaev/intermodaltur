from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from clients.models import Client
from .serializers import ClientSerializer

class ClientAPIView(APIView):

    def post(self, request, format=None):
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