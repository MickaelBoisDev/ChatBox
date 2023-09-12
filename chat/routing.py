from django.urls import re_path

from .consumers import consumers

websocket_urlpatterns = [
    # re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/rooms/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),

]
