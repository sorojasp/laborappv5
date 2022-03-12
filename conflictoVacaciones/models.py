

from django.db import models


#import models from another apps

from demandaEmpresa.models import DemandaEmpresaModel
from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from contratoLaboral.models import ContratoLaboralModel


class ConflictoPagoVacaciones(models.Model):


    fechaInicioCalculoVacaciones  = models.DateTimeField(null=True, blank=True)
    fechaFinalCalculoVacaciones = models.DateTimeField(null=True, blank=True)
    desdeCuandoNoPaganVacaciones= models.DateTimeField(null=True, blank=True)
    montoDinero_Vacaciones = models.CharField(max_length=255, null=True, blank=True)
    demandaPersonaNatural = models.ForeignKey(DemandaPersonaNaturalModel, on_delete=models.CASCADE, null=True, blank=True)
    demandaEmpresa = models.ForeignKey(DemandaEmpresaModel, on_delete=models.CASCADE, null=True, blank=True)
    contrato = models.ForeignKey(ContratoLaboralModel, on_delete=models.CASCADE,null=True, blank=True)
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
