from django.db import models
from persona.models import PersonModel
from persona_natural.models import PersonaNaturalModel
from empresa.models import EmpresaModel
# Create your models here.



class ContratoLaboralModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    tipocontrato = models.CharField(db_column='tipoContrato', max_length=100)  # Field name made lowercase.
    fechainiciocontrato = models.DateField(db_column='fechaInicioContrato')  # Field name made lowercase.
    fechafinalcontrato = models.DateField(db_column='fechaFinalContrato', blank=True, null=True)  # Field name made lowercase.
    ultimosalario = models.IntegerField(db_column='ultimoSalario')  # Field name made lowercase.
    descripcionfunciones = models.TextField(db_column='descripcionFunciones')  # Field name made lowercase.
    persona= models.ForeignKey(PersonModel, on_delete=models.CASCADE, blank=True, null=True)
    personaNatural=models.ForeignKey(PersonaNaturalModel,  on_delete=models.CASCADE, blank=True, null=True)
    empresa=models.ForeignKey(EmpresaModel,on_delete=models.CASCADE, blank=True, null=True)
    is_active= models.BooleanField(default=True)
