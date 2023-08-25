from django.contrib import admin
from django.urls import path, re_path
from user.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for My Project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="License Name"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_create/', CustomUserCreateView.as_view(), name='user_create'),
    path('get_user/', CustomUserView.as_view(), name='get_users'),
    path('token/', CustomUserTokenView.as_view(), name='token'),

    path('auth_chack_superadmin/', Auth_chack_superadmin.as_view(), name='auth_chack_superadmin'),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
