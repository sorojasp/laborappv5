from django.shortcuts import render



from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from empresa.models import EmpresaModel
from user_profile.models import Municipios


# import contrtoLaboral model

from contratoLaboral.models import ContratoLaboralModel

# import models from another modules
from persona.models import PersonModel
from persona_natural.models import PersonaNaturalModel
from empresa.models import EmpresaModel

import json
# Create your views here.


class ContratoLaboralView(APIView):


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
                find_contratoLaboral= ContratoLaboralModel.objects.filter(id=int(request.query_params.get('id')))
                print(find_contratoLaboral)
                data=find_contratoLaboral
            elif amount =='all':
                all_contratoLaboral=ContratoLaboralModel.objects.all()
                data=all_contratoLaboral

            response['data']=json.loads(serializers.serialize('json', data))
            response['result']=True
            response['detail']= "consulta exitosa"
            status=200
        except Exception as error:
            print("** error in get request  of contrato laboral:  ",error)
            response['result']=False
            response['detail']= str(error)
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

        persona_obj=None
        persona_natural_obj=None
        empresa_obj=None



        try:
            if request.data['persona_id']!='None':
                person_obj = PersonModel.objects.get(id=request.data['persona_id'])

            if request.data['personaNatural_id']!='None':
                persona_natural_obj= PersonaNaturalModel.objects.get(idPersonaNatural=request.data['personaNatural_id'])

            if request.data['empresa_id']!='None':
                empresa_obj= EmpresaModel.objects.get(id=request.data['empresa_id'])

            contrato_laboral_obj= ContratoLaboralModel.objects.create(

            tipocontrato = request.data['tipocontrato'],  # Field name made lowercase.
            fechainiciocontrato =   request.data['fechafinalcontrato'], # Field name made lowerlowercase.
            fechafinalcontrato =  request.data['fechafinalcontrato'], # Field name made lowerlowercase.
            ultimosalario =  request.data['ultimosalario'],# Field name made lowercase.
            descripcionfunciones =   request.data['descripcionfunciones'],# Field name made lowercase.
            persona= persona_obj,
            personaNatural=persona_natural_obj,
            empresa=empresa_obj



            )

            status=200
            response['result']=True
            response['data']={
                'id_contrato':contrato_laboral_obj.id
            }
        except Exception as e:
            response['details']=str(e)

        return Response(response,status=status)

    def patch(self, request,format=None,pk=None):

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

                print("data: ", request.data)


                contrato_obj=ContratoLaboralModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(contrato_obj)

                status=200
                response['result']=True
                response['detail']='Actualización realizada con éxito'

            except Exception as error:
                print("error in update process:", error)
                response['detail']=f"{str(error)}"


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
            contrato_obj=ContratoLaboralModel.objects.filter(id=int(request.query_params.get('id')))

            if len(contrato_obj)==0:
                response['detail'] ="Contrato no existe en laborapp"
            elif contrato_obj[0].is_active is False:
                response['detail'] ="Contrato ya se encuentra inactiva en laborapp"
            elif len(contrato_obj)==1 and contrato_obj[0].is_active is True:
                contrato_obj[0].is_active=False
                contrato_obj[0].save()
                status=200

                response['detail'] ="El Contrato fue dado de baja con éxito"
                response['result']=True
                response['data']=json.loads(serializers.serialize('json', contrato_obj))

        except Exception as error:
            response['detail'] = f"error:{error}"


        return Response({"data":response,},status=status)
