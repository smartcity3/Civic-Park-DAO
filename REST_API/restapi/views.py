from django.http import JsonResponse
from rest_framework.decorators import api_view
import json

# Processing function import
from .functions import processing


@api_view(['GET'])
def index(request):
    return JsonResponse({'response': 'Hello from Civic Park\'s DAO REST API'})


@api_view(['POST'])
def apriori(request):
    body_dict = json.loads(request.body.decode('utf-8'))
    support = body_dict.get('support', None)
    return JsonResponse({'apriori': processing.new_apriori(float(support), 'http://localhost:3000/api/Campaign')})


@api_view(['GET', 'POST'])
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
