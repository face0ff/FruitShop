from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from stock.consumers import CheckStockConsumer

ws_urlpatterns = [
        path("ws/check_stock/", CheckStockConsumer.as_asgi()),
    ]
