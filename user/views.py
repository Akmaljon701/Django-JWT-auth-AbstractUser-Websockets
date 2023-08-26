from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import *
from .serializers import *


class CustomUserCreateView(APIView):
    @swagger_auto_schema(request_body=CustomUserSerializer)
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user:
            serialized_user = CustomUserSerializer(request.user)
            return Response(serialized_user.data)
        else:
            return Response({'error': 'You do not have permission to access this resource'},
                            status=status.HTTP_403_FORBIDDEN)



