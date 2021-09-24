from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from persona.models import PersonModel,IdModel
from user_profile.models import UserProfile,Departamentos,Municipios

from django.core import serializers
import json 

class Personas(APIView):
    
    
    
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
                find_user=PersonModel.objects.filter(id=int(request.query_params.get('id')))
                data=find_user             
            elif amount =='all':
                all_user=PersonModel.objects.all()
                data=all_user
                
            response['data']=json.loads(serializers.serialize('json', data))
            response['result']=True
            response['detail']= "consulta exitosa"
            status=200
        except Exception as error: 
            print(error)
            response['result']=False
            response['detail']= error
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
        
        user=None
        
        
        try:
            if request.data['user_id']!='None':
                user = UserProfile.objects.get(id=request.data['user_id'])
        
            person_obj=PersonModel.objects.create(
            user=user,
            nombrespersona = request.data['nombrespersona'], 
            apellidospersona = request.data['apellidospersona'],
            fechanacimientopersona = request.data['fechanacimientopersona'],
            direccionpersona = request.data['direccionpersona'],
            generopersona = request.data['generopersona'],
            lugarresidenciapersona = Municipios.objects.get(id_municipio=request.data['lugarresidenciapersona']))
         
            
            status=200
            response['result']=True
            response['data']={
                'id_person':person_obj.id
            }            
        except Exception as e:
            response['details']=e
            
        return Response(response,status=status) 
            
            
    def patch(self,request,format=None,pk=None):
        
        status=500
        
        response={
            'result':False,
            'data':None,
            'detail':None
            }
        data_to_update={
             'email':None,
             'password':None
             }
        
        try:
            
            
            person_obj=PersonModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                        defaults=request.data)
            
            print(person_obj)
            
            status=200
            response['result']=True
            response['detail']='Actualización realizada con éxito'
            
        except Exception as error:
            print("error in update process:", error)
            response['detail']=error
            
        
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
            person_user=PersonModel.objects.filter(id=int(request.query_params.get('id')))
            
            if len(person_user)==0:
                response['detail'] ="Persona 0no existe en laborapp"
            elif person_user[0].is_active is False:
                response['detail'] ="Persona ya se encuentra inactivo en laborapp"
            elif len(person_user)==1 and person_user[0].is_active is True:
                person_user[0].is_active=False
                person_user[0].save()
                status=200
                
                response['detail'] ="El usuario fue dado de baja con éxito"
                response['result']=True
                response['data']=json.loads(serializers.serialize('json', person_user))
                
        except Exception as error:
            response['detail'] = f"error:{error}"

            
        return Response({"data":response,},status=status)