

from django.db import models


#import models from another apps

from demandaPersonaNatural.models import DemandapersonanaturalModel
from demandaEmpresa.models import DemandaempresaModel
from contrato.models import ContratoModel
from is_active.models import Is_activeModel


class Conflictopagosalario(models.Model):

    demandaPersonaNatural = models.ForeignKey(Demandapersonanatural, on_delete=models.CASCADE)
    demandaEmpresa = models.ForeignKey(Demandaempresa, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    fechaInicioNoPagoSalario = models.DateTimeField(null=True, blank=True)
    fechaFinNoPagoSalario = models.DateTimeField(null=True, blank=True)
    montoDinero_PagoSalario = models.CharField(max_length=255, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)