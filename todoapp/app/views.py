from cmath import e
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tasks
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
import datetime

def index(request):
    return HttpResponse("Hello world!")

def list_tasks(request):
    response = []
    tasks = serializers.serialize("json", Tasks.objects.all())
    tasks_json = json.loads(tasks)
    for tasks_fields in tasks_json:
        response.append(tasks_fields['fields'])
    return JsonResponse(response, content_type='application/json', safe=False)

def filter_tasks(request):
    task_body = request.GET.get("taskbody")
    task_created_time = request.GET.get("timecreated")
    found_tasks = []
    try:
        tasks = serializers.serialize("json", Tasks.objects.all())
    except Exception as e:
        return HttpResponse(e)
    tasks_json = json.loads(tasks)

    for tasks in tasks_json:
        #Filter by time
        # Date formatted as datetime.datetime(year, month, day, hour, minute), several splits are done to extract the corresponding values
        if task_created_time != None:
            date_requested = datetime.datetime(int(task_created_time.split("-")[0]), int(task_created_time.split("-")[1]), int(task_created_time.split("-")[2]), int(task_created_time.split("-")[3]), int(task_created_time.split("-")[4]))
            date_task_from_db = datetime.datetime(int(tasks["fields"]["created_at"].split("-")[0]), int(tasks["fields"]["created_at"].split("-")[1]), int(tasks["fields"]["created_at"].split("-")[2].split("T")[0]), int(tasks["fields"]["created_at"].split(":")[0].split("T")[1]), int(tasks["fields"]["created_at"].split(":")[1],),)
            if date_task_from_db == date_requested:
                found_tasks.append(tasks["fields"])
                continue
        #Filter task text body
        if task_body != None:
            if task_body in tasks["fields"]["task"]:
                found_tasks.append(tasks["fields"])

    return JsonResponse(found_tasks, safe=False)

@csrf_exempt
def create_task(request):
    res = json.loads(request.body)
    try:
        response = Tasks.objects.create(title=res["title"], task=res["task"], completed=res["completed"])
        return HttpResponse("Task created, id: {}".format(response.id))
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def delete_task(request):
    res = json.loads(request.body)
    try:
        task_to_delete = Tasks.objects.get(title=res["title"])
        task_to_delete.delete()
        return HttpResponse("Task deleted!")
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def complete_task(request):
    res = json.loads(request.body)
    try:
        task_to_complete = Tasks.objects.get(title=res["title"])
        task_to_complete.completed = True
        task_to_complete.save()
        return HttpResponse("Task marked as completed!")
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse(res["title"])