"""laborapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static


from django.conf import settings
from user_profile.views import UserProfile,UserLogin
from persona.views import Personas as PersonaView
from persona.views import IdentificationDocument
from user_profile.views import Departamentos, Municipios
from consultorioJuridico.views import ConsultorioJuridico
from persona_natural.views import PersonaNatural
from empresa.views  import EmpresaViews

from contratoLaboral.views import ContratoLaboralView
from demandaPersonaNatural.views import  DemandaPersonaNaturalViews
from archivoDemanda.views import ArchivoDemandaView
from demandaEmpresa.views import DemandaEmpresaViews
from conflictoDespidoSJC.views import ConflictoDespidoSJCViews
from conflictoPagoSalario.views import ConflictoPagoSalarioViews
from conflictoVacaciones.views import ConflictoPagoVacacionesViews
from conflictoCesantias.views import ConflictoCesantiasViews
from conflictoLiquidacion.views import ConflictoLiquidacionViews
from conflictoContactaAbogado.views import ConflictoContactaAbogadoViews
from conflictoPrimas.views import ConflictoPrimasViews
from conflictoInteresesCesantias.views import ConflictoInteresesCesantiasViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserProfile.as_view()),
    path('user/login/', UserLogin.as_view()),
    path('persona/',PersonaView.as_view()),
    path('persona/document/', IdentificationDocument.as_view()),
    path('departments/',Departamentos.as_view()),
    path('municipios/', Municipios.as_view()),
    path('consultorios/',ConsultorioJuridico.as_view()),
    path('persona-natural/',PersonaNatural.as_view()),
    path('empresa/',EmpresaViews.as_view()),
    path('contrato-laboral/', ContratoLaboralView.as_view()),
    path('demanda-persona-natural/',  DemandaPersonaNaturalViews.as_view()),
    path('archivo-demanda/', ArchivoDemandaView.as_view()),
    path('demanda-empresa/', DemandaEmpresaViews.as_view()),
    path('conflicto-despido/', ConflictoDespidoSJCViews.as_view()),
    path('conflicto-pago-salario/',ConflictoPagoSalarioViews.as_view()),
    path('conflicto-pago-vacaciones/', ConflictoPagoVacacionesViews.as_view()),
    path('conflicto-pago-cesantias/',ConflictoCesantiasViews.as_view()),
    path('conflicto-pago-liquidacion/',ConflictoLiquidacionViews.as_view()),
    path('conflicto-contacta-abogado/', ConflictoContactaAbogadoViews.as_view()),
    path('conflicto-primas/', ConflictoPrimasViews.as_view()),
    path('conflicto-intereses-cesantias/',ConflictoInteresesCesantiasViews.as_view())

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # para producción
