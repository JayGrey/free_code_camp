from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
                  path('quote/', include('quotes.urls')),
                  path('weather/', include('weather.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
