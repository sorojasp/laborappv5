from django.db import models
#from django.contrib.auth.models import User
from user.models import  MyUser as User

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    fecha = models.DateTimeField(null=False)
    porcentajeCumplimiento = models.IntegerField(null=False)
    tiempo=models.DecimalField(max_digits=2, decimal_places=1,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SubTask(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=25)
    porcentajeCumplimiento = models.IntegerField(null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)







# Create your models here.
