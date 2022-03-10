

from django.db import models


#import models from another apps



from user_profile.models import Municipios
from contratoLaboral.models import ContratoLaboralModel
from empresa.models import EmpresaModel

class DemandaEmpresaModel(models.Model):

    fechaDemandaEmpresa = models.DateTimeField(null=True, blank=True)
    codigoCiudad = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='ubicacion', blank=True, null=True)
    tipoDocumentoPersona = models.CharField(max_length=255,  null=True, blank=True)
    numeroDocumentoPersona = models.CharField(max_length=255, null=True, blank=True)
    NItEmpresa =  models.ForeignKey(EmpresaModel, models.DO_NOTHING, db_column='empresa', blank=True, null=True)
    idContrato = models.ForeignKey(ContratoLaboralModel, models.DO_NOTHING, db_column='contrato', blank=True, null=True)
    fechaPropuestaRadicacionDemandaEmpresa = models.DateTimeField(null=True, blank=True)
    fecharRealRadicacionDemandaEmpresa = models.DateTimeField(null=True, blank=True)
    fechaPropuestaRadicacionDerechoPetiEmpresa = models.DateTimeField(null=True, blank=True)
    fecharRealRadicacionDerechoPetiEmpresa = models.DateTimeField(null=True, blank=True)
    informeDesicionFinalDemandaEmpresa = models.CharField(max_length=255, null=True, blank=True)
    respuestaFinalDemandaEmpresa = models.BooleanField(default=True)
    montoTotalDemandaPersJuri = models.CharField(max_length=255, null=True, blank=True)
    superaMinimaCuantiaPersJuri = models.BooleanField(default=True)
    id = models.AutoField(primary_key=True)
    is_active=models.BooleanField(default=True)
