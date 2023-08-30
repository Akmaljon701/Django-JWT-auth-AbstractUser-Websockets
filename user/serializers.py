from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'phone',)
        extra_kwargs = {'password': {'write_only': True}}


class IsmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ism
        fields = '__all__'