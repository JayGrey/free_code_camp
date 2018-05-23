from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('quote/', include('quotes.urls')),
    path('weather/', include('weather.urls')),
]
