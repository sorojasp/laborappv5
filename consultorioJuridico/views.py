from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json 

from consultorioJuridico.models import Consultoriojuridico 

from user_profile import models as user_models
from persona import models as person_models




class ConsultorioJuridico(APIView):
     
        
    def get(self, request, *args, **kwargs):
        try:

            status=200
            amount=str(request.query_params.get('amount'))
            response={
                'result':None,
                'data':None,
                'detail':None
                }
        
            data=None
              
            if amount =='one':
                find_consultorio=Consultoriojuridico.objects.filter(idconsultoriojuridico=int(request.query_params.get('id')))
                data=find_consultorio          
            elif amount =='all':
                all_consultorios=Consultoriojuridico.objects.all()
                data=all_consultorios
                
            response['data']=json.loads(serializers.serialize('json', data))
            response['result']=True
            response['detail']= "consulta exitosa"
            status=200
        except Exception as error: 
            print(error)
            response['result']=False
            response['detail']=str(error)
            status=500
        
        return Response({"data":response,
                        },status=status)
    
    
    def post(self, request, *args, **kwargs):
        
        status=500
        
        response={
            'result':False,
            'data':None,
            'detail':None
            }
        
        person_obj=None
        ciudad_obj=None
        
        
        try:
            if request.data['person_id']!='None':
                person_obj = person_models.PersonModel.objects.get(id=request.data['person_id'])
                
            if request.data['ciudad_id']!='None':
                ciudad_obj = user_models.Municipios.objects.get(id_municipio=request.data['ciudad_id'])
                
          
            consultorio_obj=Consultoriojuridico.objects.create(
               
                tipoconsultoriojuridico = request.data['tipoconsultoriojuridico'],
                nombreconsultoriojuridico = request.data['nombreconsultoriojuridico'],
                telefonoconsultoriojuridico = request.data['telefonoconsultoriojuridico'],
                emailconsultoriojuridico = request.data['emailconsultoriojuridico'],
                direccionconsultoriojuridico = request.data['direccionconsultoriojuridico'],
                personaencargada = person_obj,
                ciudad = ciudad_obj
                
                )
            consultorio_obj.save()
            
         
            
            status=200
            response['result']=True
            response['data']={
                'id_document': consultorio_obj.idconsultoriojuridico
            }            
        except Exception as e:
            response['details']=str(e)
            print(e)
            
        return Response(response,status=status) 
            
            
    def patch(self,request,format=None,pk=None):
        
        status=500
        
        response={
            'result':False,
            'data':None,
            'detail':None
            }

        
        try:
            
            print("data: ", request.data)
            print("document: ", request.query_params.get('id'))
            document_obj=Consultoriojuridico.objects.update_or_create(idconsultoriojuridico =request.query_params.get('id'),
                                                                        defaults=request.data)
            
            print(document_obj)
            
            
            status=200
            response['result']=True
            response['detail']='Actualización realizada con éxito'
            
        except Exception as error:
            print("error in update process:", error)
            response['detail']=str(error)
            
        
        return Response(response,status=status)
    
    
    def delete(self,request,format=None,pk=None):
        
        status=500
        
        response={
            'result':False,
            'data':None,
            'detail':None
            }
        
        try:
            id=request.query_params.get('id')
            obj_consultorio=Consultoriojuridico.objects.filter(idconsultoriojuridico=int(id))
            
            if len(obj_consultorio)==0:
                response['detail'] ="Consultorio Jurídico no existe en laborapp"
            elif obj_consultorio[0].is_active is False:
                response['detail'] ="Consultorio Jurídico ya se encuentra inactivo en laborapp"
            elif len(obj_consultorio)==1 and obj_consultorio[0].is_active is True:
                obj_consultorio[0].is_active=False
                obj_consultorio[0].save()
                status=200
                
                response['detail'] ="El Consultorio Jurídico fué dado de baja con éxito"
                response['result']=True
                response['data']=json.loads(serializers.serialize('json', obj_consultorio))
                
        except Exception as error:
            response['detail'] = f"error:{str(error)}"

            
        return Response({"data":response,},status=status)
            
        
        
