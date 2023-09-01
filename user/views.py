from asgiref.sync import async_to_sync
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
import uuid
from .consumers import IsmlarConsumer
from channels.layers import get_channel_layer
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


class IsmView(APIView):
    parser_classes = [MultiPartParser]  # Fayllarni qabul qilish uchun MultiPartParser qo'shamiz

    @swagger_auto_schema(request_body=IsmSerializer)
    def post(self, request):
        serializer = IsmSerializer(data=request.data)
        if serializer.is_valid():
            name = request.data.get('name')
            rasm = request.data.get('rasm')

            if rasm is not None:
                rasm = f"{uuid.uuid4()}-{rasm}"  # Fayl nomini generatsiya qilish (hechqachon birhil bo'lmaydi shunda)
                serializer.save(rasm=rasm)
            else:
                serializer.save()

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "ism_group",  # WebSocket guruhi nomi (shu bo'yicha consumersdan qaysi websocketga jo'natish ajratib olinadi)
                {
                    "type": "add_new_ism",   # wensocket tomindagi yangi malumot kelganini qabul qilib oladigan funksiya
                },
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IsmDeleteAPIView(APIView):
    @swagger_auto_schema(request_body=IdListSerializer)
    def delete(self, request):
        # JSON formatida id lar listini olish
        serializer = IdListSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        ids_to_delete = serializer.validated_data['ids']

        # Malumotlarni o'chirish
        Ism.objects.filter(id__in=ids_to_delete).delete()

        return Response({'message': 'Malumotlar o\'chirildi'}, status=status.HTTP_204_NO_CONTENT)