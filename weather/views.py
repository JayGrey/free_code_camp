from django.http import JsonResponse


def index(request):
    json = JsonResponse({})
    # adding CORS support
    json['Access-Control-Allow-Origin'] = '*'
    return json
