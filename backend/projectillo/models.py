from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

import datetime
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    def __str__(self):
        return f'username: {self.user.username}'
    

class Tasks(models.Model):
    status = ( 
              ('Not Started','Not Started'),
              ('In Progress', 'In Progress'),
              ('Complete','Complete')
              )
    
    status = models.CharField(max_length=12, choices=status, default='')
    Task_Name = models.CharField(max_length=20, default='')
    Description = models.TextField(max_length=450, default='')
    due_date = models.DateField(null=True)
    
    
    def __str__(self):
        return f'{self.Task_Name}'


class Projects(models.Model):
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.SET_NULL, null=True)
    project_name = models.TextField(max_length=60)
    description = models.TextField(max_length=150, null=True)
    deadline = models.DateTimeField(null=True)
    tasks = models.ForeignKey(Tasks, related_name="Task", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.project_name}, {self.owner.username}, {self.description}, {self.tasks}'