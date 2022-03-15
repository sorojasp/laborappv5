

from django.db import models


#import models from another apps


from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from demandaEmpresa.models import DemandaEmpresaModel



class ConflictoContactaAbogadoModel(models.Model):

    conflictoARL = models.BooleanField(default=False, null=True, blank=True)
    conflictoPensiones = models.BooleanField(default=False, null=True, blank=True)
    conflictoHorasExtras = models.BooleanField(default=False, null=True, blank=True)
    conflictoDominicalesFestivos = models.BooleanField(default=False, null=True, blank=True)
    demandaPersonaNatural = models.ForeignKey(DemandaPersonaNaturalModel, on_delete=models.CASCADE, null=True, blank=True)
    demandaEmpresa = models.ForeignKey(DemandaEmpresaModel, on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
