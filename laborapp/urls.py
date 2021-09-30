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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserProfile.as_view()),
    path('user/login/', UserLogin.as_view()),
    path('persona/',PersonaView.as_view()),
    path('persona/document/', IdentificationDocument.as_view()),
    path('departments/',Departamentos.as_view()),
    path('municipios/', Municipios.as_view()),
    path('consultorios/',ConsultorioJuridico.as_view() )
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # para producción
