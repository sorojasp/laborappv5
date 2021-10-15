from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response


from empresa.models import EmpresaModel
from user_profile.models import Municipios
from persona.models import PersonModel




import json

class EmpresaViews(APIView):




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
                find_empresa= EmpresaModel.objects.filter(id=int(request.query_params.get('id')))
                print(find_empresa)
                data=find_empresa
            elif amount =='all':
                all_empresa=EmpresaModel.objects.all()
                data=all_empresa

            response['data']=json.loads(serializers.serialize('json', data))
            response['result']=True
            response['detail']= "consulta exitosa"
            status=200
        except Exception as error:
            print("** error in get request  of empresa:  ",error)
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

        persona=None
        municipio=None


        try:
            if request.data['persona_id']!='None':
                person = PersonModel.objects.get(id=request.data['persona_id'])

            if request.data['municipio_id']!='None':
                municipio=Municipios.objects.get(id_municipio= request.data['municipio_id'])

                empresa_obj=EmpresaModel.objects.create(
                NItEmpresa = request.data['NItEmpresa'],
                nombreEmpresaRS= request.data['nombreEmpresaRS'],
                telefonoEmpresa= request.data['telefonoEmpresa'],
                direccionEmpresa= request.data['direccionEmpresa'],
                emailEmpresa= request.data['emailEmpresa'],
                ubicacion=municipio,
                persona= person
                )


            status=200
            response['result']=True
            response['data']={
                'id_empresa_obj':empresa_obj.id
            }
        except Exception as e:
            response['details']=str(e)

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

            print("data: ", request.data)


            empresa_obj=EmpresaModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                        defaults=request.data)

            print(empresa_obj)

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
            empresa_obj=EmpresaModel.objects.filter(id=int(request.query_params.get('id')))

            if len(empresa_obj)==0:
                response['detail'] ="Empresa no existe en laborapp"
            elif empresa_obj[0].is_active is False:
                response['detail'] ="Empresa ya se encuentra inactiva en laborapp"
            elif len(empresa_obj)==1 and empresa_obj[0].is_active is True:
                empresa_obj[0].is_active=False
                empresa_obj[0].save()
                status=200

                response['detail'] ="El Empresa fue dada de baja con éxito"
                response['result']=True
                response['data']=json.loads(serializers.serialize('json', empresa_obj))

        except Exception as error:
            response['detail'] = f"error:{error}"


        return Response({"data":response,},status=status)


# Create your views here.
