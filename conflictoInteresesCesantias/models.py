

from django.db import models


#import models from another apps

from demandaEmpresa.models import DemandaEmpresaModel
from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from contratoLaboral.models import ContratoLaboralModel



class ConflictoInteresesCesantiasModel(models.Model):


    fechaUltimasCesantiasPagadas  = models.DateTimeField(null=True, blank=True)
    fechaFinalNoPagoCesantias= models.DateTimeField(null=True, blank=True)
    desdeCuandoNoPaganCesantias= models.DateTimeField(null=True, blank=True)
    montoDinero_Cesantias = models.CharField(max_length=255, null=True, blank=True)
    montoDinero_InteresesCesantias = models.CharField(max_length=255, null=True, blank=True)
    anios=models.CharField(max_length=255, null=True, blank=True)
    cantidadesPorAnio=models.CharField(max_length=255, null=True, blank=True)
    demandaPersonaNatural = models.ForeignKey(DemandaPersonaNaturalModel, on_delete=models.CASCADE, null=True, blank=True)
    demandaEmpresa = models.ForeignKey(DemandaEmpresaModel, on_delete=models.CASCADE, null=True, blank=True)
    contrato = models.ForeignKey(ContratoLaboralModel, on_delete=models.CASCADE,null=True, blank=True)
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
