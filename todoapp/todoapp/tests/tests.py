from asyncio import Task
import pytest
from django.core import serializers
import json
import datetime

from app.models import Tasks


@pytest.mark.django_db
def test_list_tasks():
    tasks = ["task1", "task2", "task3"]

    for task in tasks:
        Tasks.objects.create(title = task, task = "A great task to do", completed = False)

    list_tasks = serializers.serialize("json", Tasks.objects.all())
    tasks_json = json.loads(list_tasks)
    assert len(tasks_json) == 3

@pytest.mark.django_db
def test_task_creation():

    task = Tasks.objects.create(
        title = "task1000",
        task = "A great task to do",
        completed = False
    )

    assert task.title == "task1000"

@pytest.mark.django_db
def test_task_delete():
    title = "task1"
    
    task = Tasks.objects.create(
        title = title,
        task = "A great task to do",
        completed = False
    )

    task_created = Tasks.objects.get(title=title)

    task_created.delete()

@pytest.mark.django_db
def test_task_mark_complete():
    title = "task1000"

    task = Tasks.objects.create(
        title = title,
        task = "A great task to do",
        completed = False
    )

    task_to_complete = Tasks.objects.get(title=title)
    task_to_complete.completed=True
    task_to_complete.save()

    task_completed = Tasks.objects.get(title=title)

    assert task_completed.completed == True