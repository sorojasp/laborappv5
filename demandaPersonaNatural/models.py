from django.db import models



from user_profile.models import Municipios
from persona.models import PersonModel
from persona_natural.models import PersonaNaturalModel
from contratoLaboral.models import ContratoLaboralModel


class DemandaPersonaNaturalModel(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    fechademandapersonanatural = models.DateField(db_column='fechaDemandaPersonaNatural', blank=True, null=True)  # Field name made lowercase.

    ubicacion = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='ubicacion', blank=True, null=True)  # Field name made lowercase.
    personanatural = models.ForeignKey(PersonaNaturalModel, models.DO_NOTHING, db_column='personaNatural', blank=True, null=True)  # Field name made lowercase.
    contrato = models.ForeignKey(ContratoLaboralModel, models.DO_NOTHING, db_column='contrato', blank=True, null=True)  # Field name made lowercase.
    demandante= models.ForeignKey(PersonModel, models.DO_NOTHING, db_column='demandante', blank=True, null=True) # Field name made lower

    fechapropuestaradicaciondemandapersonan = models.DateField(db_column='fechaPropuestaRadicacionDemandaPersonaN', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicaciondemandapersonan = models.DateField(db_column='fecharRealRadicacionDemandaPersonaN', blank=True, null=True)  # Field name made lowercase.
    fechapropuestaradicacionderechopetipersonan = models.DateField(db_column='fechaPropuestaRadicacionDerechoPetiPersonaN', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicacionderechopetipersonan = models.DateField(db_column='fecharRealRadicacionDerechoPetiPersonaN', blank=True, null=True)  # Field name made lowercase.
    informedesicionfinaldemandapersonan = models.TextField(db_column='informeDesicionFinalDemandaPersonaN', blank=True, null=True)  # Field name made lowercase.
    respuestafinaldemandaersonan = models.TextField(db_column='respuestaFinalDemandaersonaN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    montototaldemandapersnat = models.FloatField(db_column='montoTotalDemandaPersNat', blank=True, null=True)  # Field name made lowercase.
    superaminimacuantiapersnat = models.TextField(db_column='superaMinimaCuantiaPersNat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    is_active=models.BooleanField(default=True)

# Create your models here.
