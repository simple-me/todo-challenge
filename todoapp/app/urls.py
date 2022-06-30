from asyncio import create_task
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.list_tasks, name='tasks'),
    path('tasks/create', views.create_task, name='create'),
    path('tasks/delete', views.delete_task, name='delete'),
    path('tasks/complete', views.complete_task, name='complete'),
    path('tasks/search', views.filter_tasks, name='search')
]
