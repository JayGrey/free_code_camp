from datetime import datetime

from django.conf import settings

import requests


def get_server_name(request):
    port = ':' + request.META['SERVER_PORT'] if request.META['SERVER_PORT'] != 80 else ''
    return '{}://{}{}'.format(request.scheme, request.META['SERVER_NAME'], port)


def get_background_image(date, phenomenon):
    if date.month in (12, 1, 2):
        season = 'winter'
    elif date.month in (3, 4, 5):
        season = 'spring'
    elif date.month in (6, 7, 8):
        season = 'summer'
    else:
        season = 'autumn'

    if phenomenon != 'rain' and phenomenon != 'clouds':
        phenomenon = 'clearsky'

    return '{}{}/{}-{}.jpg'.format(settings.STATIC_URL, 'weather', season, phenomenon)


def get_data_from_server(request):
    latitude = request.GET.get("latitude")
    longitude = request.GET.get("longitude")

    json = requests.get(settings.WEATHER_SERVER,
                        params={'lat': latitude, 'lon': longitude}).json()

    bg_image = '{}{}'.format(get_server_name(request), get_background_image(datetime.today(), request))

    response = {
        'latitude': latitude,
        'longitude': longitude,
        'temperature': json['main']['temp'],
        'pressure': json['main']['pressure'],
        'humidity': json['main']['humidity'],
        'weather_short': json['weather'][0]['main'],
        'weather_long': json['weather'][0]['description'],
        'weather_icon': json['weather'][0]['icon'],
        'background_image': bg_image,
        'place': json['name'] + ', ' + json['sys']['country'],
    }

    return response
