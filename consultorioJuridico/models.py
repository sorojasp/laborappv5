from django.db import models
from user_profile import models as user_models
from persona import models as person_models



# Create your models here.
class Consultoriojuridico(models.Model):
    idconsultoriojuridico = models.AutoField(db_column='IdconsultorioJuridico', primary_key=True)  # Field name made lowercase.
    tipoconsultoriojuridico = models.CharField(db_column='tipoConsultorioJuridico', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombreconsultoriojuridico = models.CharField(db_column='nombreConsultorioJuridico', max_length=300)  # Field name made lowercase.
    telefonoconsultoriojuridico = models.IntegerField(db_column='telefonoConsultorioJuridico')  # Field name made lowercase.
    emailconsultoriojuridico = models.EmailField(db_column='emailConsultorioJuridico', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccionconsultoriojuridico = models.CharField(db_column='direccionConsultorioJuridico', max_length=200, blank=True, null=True)  # Field name made lowercase.
    personaencargada = models.ForeignKey(person_models.PersonModel,  on_delete=models.CASCADE,blank=True, null=True) 
    ciudad = models.ForeignKey(user_models.Municipios,  on_delete=models.CASCADE,blank=True, null=True)  # Field name made lowercase.
    is_active=models.BooleanField(default=True)
