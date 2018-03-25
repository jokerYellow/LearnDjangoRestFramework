from django.db import models

# Create your models here.

class TodoCategory(models.Model):
    name = models.CharField(max_length=100)

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(TodoCategory,on_delete=models.CASCADE)
