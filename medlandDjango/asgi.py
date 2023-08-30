import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medlandDjango.settings')

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
import chat.routing
import user.routing


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            user.routing.websocket_urlpatterns +
            chat.routing.websocket_urlpatterns
        )
    )
})
# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# import chat.routing
# import user.routing
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medlandDjango.settings')
#
# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             user.routing.websocket_urlpatterns,
#             chat.routing.websocket_urlpatterns
#         )
#     )
# })
