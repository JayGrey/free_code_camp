from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Quote


def index(request):
    quote = Quote.quotes.random()
    response = {'author': quote.author, 'text': quote.text}
    json = JsonResponse(response)
    # adding CORS support
    json['Access-Control-Allow-Origin'] = '*'
    return json
