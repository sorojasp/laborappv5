from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from personas.models import PersonModel,IdModel
from user_profile.models import UserProfile,Departamentos,Municipios

class Personas(APIView):
    
    
    
    def get(self, request, *args, **kwargs):
        
        return Response({'api':"Personas"},200)
    
    def post(self, request, *args, **kwargs):
        
        person_obj=PersonModel.objects.create(
             user= None,
             nombrespersona = request.data['nombrespersona'], 
             apellidospersona = request.data['apellidospersona'],
             fechanacimientopersona = request.data['fechanacimientopersona'],
             direccionpersona = request.data['direccionpersona'],
             generopersona = request.data['generopersona'],
             lugarresidenciapersona = Municipios.objects.get(id_municipio=request.data['lugarresidenciapersona'])
             
             )
        print(person_obj)
        #person_obj.save()
        #print(person_obj)
        
        
        return Response({'api':"Personas"},200)
        

# Create your views here.
