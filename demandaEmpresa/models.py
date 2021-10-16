from django.db import models

# Create your models here.



class Demandaempresa(models.Model):
    iddemandaempresa = models.AutoField(db_column='idDemandaEmpresa', primary_key=True)  # Field name made lowercase.
    fechademandaempresa = models.DateField(db_column='fechaDemandaEmpresa')  # Field name made lowercase.
    codigociudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='codigoCiudad')  # Field name made lowercase.
    tipodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='tipoDocumentoPersona')  # Field name made lowercase.
    numerodocumentopersona = models.ForeignKey('Personas', models.DO_NOTHING, db_column='numeroDocumentoPersona')  # Field name made lowercase.
    nitempresa = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='NItEmpresa')  # Field name made lowercase.
    idcontrato = models.ForeignKey(Contratolaboral, models.DO_NOTHING, db_column='idContrato')  # Field name made lowercase.
    fechapropuestaradicaciondemandaempresa = models.DateField(db_column='fechaPropuestaRadicacionDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicaciondemandaempresa = models.DateField(db_column='fecharRealRadicacionDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.
    fechapropuestaradicacionderechopetiempresa = models.DateField(db_column='fechaPropuestaRadicacionDerechoPetiEmpresa', blank=True, null=True)  # Field name made lowercase.
    fecharrealradicacionderechopetiempresa = models.DateField(db_column='fecharRealRadicacionDerechoPetiEmpresa', blank=True, null=True)  # Field name made lowercase.
    informedesicionfinaldemandaempresa = models.TextField(db_column='informeDesicionFinalDemandaEmpresa', blank=True, null=True)  # Field name made lowercase.
    respuestafinaldemandaempresa = models.TextField(db_column='respuestaFinalDemandaEmpresa', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    montototaldemandapersjuri = models.FloatField(db_column='montoTotalDemandaPersJuri', blank=True, null=True)  # Field name made lowercase.
    superaminimacuantiapersjuri = models.TextField(db_column='superaMinimaCuantiaPersJuri', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
