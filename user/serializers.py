from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from rest_framework.exceptions import ValidationError


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'first_name', 'phone',)
        extra_kwargs = {'password': {'write_only': True}}


class IsmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ism
        fields = '__all__'

    def validate_rasm(self, value):
        allowed_extensions = ('.png', '.jpg', '.jpeg')
        if not value.name.lower().endswith(allowed_extensions):
            raise ValidationError("Fayl formati noto'g'ri. Faqat .png, .jpg yoki .jpeg formatlarni qabul qilinadi.")
        return value


class IdListSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField())