from django.contrib import admin
from django.urls import path, include
from user.views import *
from .swagger import schema_view

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user_create/', CustomUserCreateView.as_view(), name='user_create'),
    path('user_get/', CustomUserView.as_view(), name='get_users'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('ism_create/', IsmView.as_view(), name='ism'),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('', include('chat.urls')),
]
