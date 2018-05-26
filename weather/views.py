from django.http import JsonResponse

from .utils import get_data_from_server


def index(request):
    response = get_data_from_server(request.GET.get('latitude'),
                                    request.GET.get('longitude'))

    json = JsonResponse(response)
    # adding CORS support
    json['Access-Control-Allow-Origin'] = '*'
    return json
