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

def getQa(request, pk):
    if request.method == 'GET':
        try:
            question = Qa.objects.get(id = pk)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        json_task = question.get_questions()
        return JsonResponse(json_task)

def getQaG(request, pk):
    if request.method == 'GET':
        try:
            groups = Group.objects.get(id = pk)
        except Group.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        qa = groups.qa_set.all()
        json_qa = [tk.get_questions() for tk in qa]
        return JsonResponse(json_qa, safe = False)

def getUser(request, nameTemp):
    if request.method == 'GET':
        try:
            user = User.objects.get(name = nameTemp)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        json_user = user.get_user()
        return JsonResponse(json_user, safe= False)

def getUserPoints(request, nameTemp):
    if request.method == 'GET':
        try:
            user = User.objects.get(name = nameTemp)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        json_user = user.get_user_points()
        return JsonResponse(json_user, safe= False)

def getUserGroupPoints(request, idUserTemp, pk):
    if request.method == 'GET':
        try:
            group = Data.objects.get(id_user = idUserTemp, id_group = pk)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        json_user = group.get_group_points()
        return JsonResponse(json_user, safe= False)

def checkPassword(request, nameTemp, passwordTemp):
    if request.method == 'GET':
        try:
            user = User.objects.get(name = nameTemp)
        except Qa.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

        is_equal = {'is_equal':False}
        password = user.get_password()
        if password['password'] == passwordTemp:
            is_equal['is_equal'] = True
        return JsonResponse(is_equal, safe= False)