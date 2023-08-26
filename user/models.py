from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13)
    active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, default="user")


class Test(models.Model):
    name = models.CharField(max_length=100)