

from django.db import models


#import models from another apps

from ubicacion.models import UbicacionModel
from personaNatural.models import PersonanaturalModel
from contrato.models import ContratoModel


class Demandapersonanatural(models.Model):

    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    personaNatural = models.ForeignKey(Personanatural, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
     fechapropuestaradicaciondemandapersonan = models.DateTimeField(null=True)
     fecharrealradicaciondemandapersonan = models.DateTimeField(null=True)
    fechapropuestaradicacionderechopetipersona = models.DateTimeField(null=True)
     fecharrealradicacionderechopetipersonan = models.DateTimeField(null=True)
    informedesicionfinaldemandapersonan = models.CharField(max_length=255, unique=True, null=True)
    respuestafinaldemandaersonan = models.CharField(max_length=255, unique=True, null=True)
    montototaldemandapersnat = models.DecimalField(max_digits=5, decimal_places=2)
    superaminimacuantiapersna = models.CharField(max_length=255, unique=True, null=True)