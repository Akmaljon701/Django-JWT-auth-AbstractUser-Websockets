from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .serializers import *


class CustomUserTokenView(APIView):
    @swagger_auto_schema(request_body=CustomTokenSerializer)
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = get_user_model().objects.get(username=username)
            if not user.check_password(password):
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except get_user_model().DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        refresh = RefreshToken.for_user(user)
        serialized_user = CustomTokenSerializer(user).data

        return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user': serialized_user})


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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user:
            serialized_user = CustomUserSerializer(request.user)
            return Response(serialized_user.data)
        else:
            return Response({'error': 'You do not have permission to access this resource'},
                            status=status.HTTP_403_FORBIDDEN)


class Auth_chack_superadmin(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role == 'superadmin':
            return Response("Auth ishlayabti!")
        else:
            return Response("Role superadmin emas lekin auth ishlayabti!")



