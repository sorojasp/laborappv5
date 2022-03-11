

from django.db import models


#import models from another apps

from demandaEmpresa.models import DemandaEmpresaModel
from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from contratoLaboral.models import ContratoLaboralModel


class ConflictoPagoSalarioModel(models.Model):

    demandaPersonaNatural = models.ForeignKey(DemandaPersonaNaturalModel, on_delete=models.CASCADE, null=True, blank=True)
    demandaEmpresa = models.ForeignKey(DemandaEmpresaModel, on_delete=models.CASCADE, null=True, blank=True)
    contrato = models.ForeignKey(ContratoLaboralModel, on_delete=models.CASCADE,null=True, blank=True)
    fechaInicioNoPagoSalario = models.DateTimeField(null=True, blank=True)
    fechaFinNoPagoSalario = models.DateTimeField(null=True, blank=True)
    montoDinero_PagoSalario = models.CharField(max_length=255, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
