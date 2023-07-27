from django.core.asgi import get_asgi_application
from django.urls import path, re_path
from channels.routing import ProtocolTypeRouter, URLRouter

from bank.consumers import ChangeBankConsumer
from chat.consumers import ChatConsumer, JokeConsumer
from stock.consumers import CheckStockConsumer, ChangeStockConsumer

ws_urlpatterns = [
        path("ws/check_stock/", CheckStockConsumer.as_asgi()),
        path("ws/updates/", ChangeBankConsumer.as_asgi()),
        path("ws/updates_stock/", ChangeStockConsumer.as_asgi()),
        path("ws/chat/", ChatConsumer.as_asgi()),
        path("ws/joke/", JokeConsumer.as_asgi()),
    ]
