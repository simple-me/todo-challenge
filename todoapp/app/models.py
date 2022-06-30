from operator import truediv
from django.db import models

class Tasks(models.Model):
  title = models.CharField(max_length=50, null=True, unique=True)
  task = models.CharField(max_length=300, null=True)
  completed = models.BooleanField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)