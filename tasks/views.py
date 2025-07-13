from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

def task_list(request):
    tasks = Task.objects.all().values()
    return JsonResponse(list(tasks), safe=False)

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            task = Task.objects.create(title=data['title'])
            return JsonResponse({'id': task.id, 'title': task.title})
        except (KeyError, json.JSONDecodeError):
            return HttpResponseBadRequest("Invalid data")
    else:
        return HttpResponseBadRequest("Only POST requests are allowed")
