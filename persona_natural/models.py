from django.db import models
from persona import models as person_model

# Create your models here.

class PersonaNaturalModel(models.Model):
     idPersonaNatural = models.AutoField(primary_key=True)
     person = models.ForeignKey(person_model.PersonModel, on_delete=models.CASCADE,blank=True, null=True)
    