import requests

from django.conf import settings


def get_data_from_server(latitude, longitude):
    json = requests.get(settings.WEATHER_SERVER,
                        params={'lat': latitude, 'lon': longitude}).json()

    response = {
        'latitude': latitude,
        'longitude': longitude,
        'temperature': json['main']['temp'],
        'pressure': json['main']['pressure'],
        'humidity': json['main']['humidity'],
        'weather_short': json['weather'][0]['main'],
        'weather_long': json['weather'][0]['description'],
        'weather_icon': json['weather'][0]['icon'],
        'background_image': '',
        'place': json['name'] + ', ' + json['sys']['country'],
    }

    return response
