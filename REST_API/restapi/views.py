from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view

# Processing function import
from .functions import processing


@api_view(['GET'])
@ensure_csrf_cookie
def index(request):
    return JsonResponse({'response': 'Hello from Civic Park\'s DAO REST API'})


@api_view(['GET'])
@ensure_csrf_cookie
def campaigns(request):
    return JsonResponse({'campaigns': processing.get_campaign_data_from_response()})

