from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'first_name', 'phone', 'active', 'role']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('phone', 'active', 'role')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


class IsmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rasm']  # Ko'rsatiladigan maydonlar ro'yxati


admin.site.register(Ism, IsmAdmin)
