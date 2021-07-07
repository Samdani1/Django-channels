## urls.py
from django.urls import path
from .views import index, send_data, rdata

urlpatterns = [
    ## ... Other URLS
    path('', index),
    path('send/data', rdata, name = "validate_nickname"),
]