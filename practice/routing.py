from django.urls import re_path
from .consumers import PracticeConsumer

websocket_urlpatterns = [
    re_path(r'', PracticeConsumer.as_asgi()),
]
