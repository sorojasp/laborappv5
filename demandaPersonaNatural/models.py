from django.db import models



class Demandapersonanatural(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    fechademandapersonanatural = models.DateField(db_column='fechaDemandaPersonaNatural')  # Field name made lowercase.
    codigociudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='codigoCiudad')  # Field name made lowercase.
    idpersonanatural = models.ForeignKey('Personanatural', models.DO_NOTHING, db_column='IdPersonaNatural')  # Field name made lowercase.
    idcontrato = models.ForeignKey(Contratolaboral, models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    fechapropuestaradicaciondemandapersonan = models.DateField(db_column='fechaPropuestaRadicacionDemandaPersonaN', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicaciondemandapersonan = models.DateField(db_column='fecharRealRadicacionDemandaPersonaN', blank=True, null=True)  # Field name made lowercase.
    fechapropuestaradicacionderechopetipersonan = models.DateField(db_column='fechaPropuestaRadicacionDerechoPetiPersonaN', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicacionderechopetipersonan = models.DateField(db_column='fecharRealRadicacionDerechoPetiPersonaN', blank=True, null=True)  # Field name made lowercase.
    informedesicionfinaldemandapersonan = models.TextField(db_column='informeDesicionFinalDemandaPersonaN', blank=True, null=True)  # Field name made lowercase.
    respuestafinaldemandaersonan = models.TextField(db_column='respuestaFinalDemandaersonaN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    montototaldemandapersnat = models.FloatField(db_column='montoTotalDemandaPersNat', blank=True, null=True)  # Field name made lowercase.
    superaminimacuantiapersnat = models.TextField(db_column='superaMinimaCuantiaPersNat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

# Create your models here.
