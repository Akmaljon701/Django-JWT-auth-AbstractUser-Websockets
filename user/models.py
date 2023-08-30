from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13)
    active = models.BooleanField(default=True)
    role = models.CharField(max_length=20, default="user")


class Ism(models.Model):
    name = models.CharField(max_length=100)