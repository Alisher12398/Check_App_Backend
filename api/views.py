from django.shortcuts import render
from .models import User, Qa, Group, Data
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def getQroups(request):
    if request.method == 'GET':
        groups = Group.objects.all()
        json_groups = [t.get_groups() for t in groups]
        return JsonResponse(json_groups, safe=False)
    # elif request.method == 'POST':
    #     body = json.loads(request.body)
    #     if 'name' in body:
    #         taskList = TaskList(name = body['name'])
    #         taskList.save()
    #         return JsonResponse(taskList.to_json())
    return JsonResponse({'error': 'bad request'})

