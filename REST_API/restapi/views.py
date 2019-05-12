from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view

# Processing function import
from .functions import processing


@api_view(['GET'])
@ensure_csrf_cookie
def index(request):
    return JsonResponse({'response': 'Hello from Civic Park\'s DAO REST API'})


@api_view(['GET', 'POST'])
@ensure_csrf_cookie
def campaigns(request):
    if request.method == 'GET':
        campaign_id = request.get_raw_uri().split('/')[-1]
        if campaign_id.isdigit():
            return JsonResponse({'campaigns': processing.get_json('http://localhost:3000/api/Campaign/{id}'.
                                                                  format(id=campaign_id))})
        else:
            return JsonResponse({'campaigns': processing.get_json('http://localhost:3000/api/Campaign')})
    elif request.method == 'POST':
        return JsonResponse({'campaigns': processing.post_json(request.body, 'http://localhost:3000/api/Campaign')})


@api_view(['GET', 'POST'])
@ensure_csrf_cookie
def teams(request):
    if request.method == 'GET':
        team_id = request.get_raw_uri().split('/')[-1]
        if team_id.isdigit():
            return JsonResponse({'teams': processing.get_json('http://localhost:3000/api/Team/{id}'.
                                                              format(id=team_id))})
        else:
            return JsonResponse({'teams': processing.get_json('http://localhost:3000/api/Team')})
    elif request.method == 'POST':
        return JsonResponse({'teams': processing.post_json(request.body, 'http://localhost:3000/api/Team')})
