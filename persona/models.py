from django.db import models
from user_profile import models as user_profile_models

# Create your models here.


class PersonModel(models.Model):

    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(user_profile_models.UserProfile, on_delete=models.CASCADE,blank=True, null=True)
    nombrespersona = models.CharField(db_column='nombresPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    apellidospersona = models.CharField(db_column='apellidosPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    fechanacimientopersona = models.DateField(db_column='fechaNacimientoPersona', blank=True, null=True)  # Field name made lowercase.
    direccionpersona = models.CharField(db_column='direccionPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    generopersona = models.CharField(db_column='generoPersona', max_length=70, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='phone', max_length=70, blank=True, null=True)  # Field name made lowercase.
    lugarresidenciapersona =  models.ForeignKey(user_profile_models.Municipios, on_delete=models.CASCADE,  blank=True, null=True)
    is_active=models.BooleanField(default=True)



class IdModel(models.Model):

    id = models.AutoField(primary_key=True)
    persona=models.ForeignKey(PersonModel, on_delete=models.CASCADE,blank=True, null=True)
    tipodocumentopersona = models.CharField(db_column='tipoDocumentoPersona',  max_length=70, blank=True, null=True)  # Field name made lowercase.
    numerodocumentopersona = models.IntegerField(db_column='numeroDocumentoPersona', blank=True, null=True)  # Field name made lowercase.
    lugarexpedicioncedulapersona =  models.ForeignKey(user_profile_models.Municipios, on_delete=models.CASCADE, blank=True, null=True)
    fechaexpedicioncedulapersona = models.DateTimeField(null=True , blank=True)
    haveColombianId=models.BooleanField(null=True , blank=True,default=True)
    country=models.CharField(db_column='country',  max_length=70, blank=True, null=True)
