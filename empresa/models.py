from django.db import models
from django.db.models.deletion import CASCADE
from persona.models import PersonModel
from user_profile.models import Municipios 


# Create your models here.


class EmpresaModel(models.Model):
    
    id= models.AutoField(primary_key=True)
    NItEmpresa = models.CharField(max_length=255, null=True, blank=True)
    nombreEmpresaRS= models.CharField(max_length=255, null=True, blank=True)
    telefonoEmpresa= models.CharField(max_length=255, null=True, blank=True)
    direccionEmpresa= models.CharField(max_length=255, null=True, blank=True)
    telefonoEmpresa= models.CharField(max_length=255, null=True, blank=True)
    emailEmpresa= models.EmailField(null=True, blank=True)
    is_active= models.BooleanField(default=True)
    ubicacion=models.ForeignKey(Municipios, on_delete=models.CASCADE,  blank=True, null=True)
    persona= models.ForeignKey(PersonModel, on_delete=models.CASCADE,  blank=True, null=True)
    
