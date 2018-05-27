from django.http import JsonResponse

from .utils import get_data_from_server


def index(request):
    response = get_data_from_server(request)

    json = JsonResponse(response)
    # adding CORS support
    json['Access-Control-Allow-Origin'] = '*'
    return json
