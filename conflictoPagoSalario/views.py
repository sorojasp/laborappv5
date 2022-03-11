

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from conflictoPagoSalario.models import ConflictoPagoSalarioModel

import json

#import models from another apps

from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from demandaEmpresa.models import DemandaEmpresaModel
from contratoLaboral.models import ContratoLaboralModel





class ConflictoPagoSalarioViews(APIView):



        queryset = ConflictoPagoSalarioModel.objects.all()



        def get(self, request,  format=None, *args, **kwargs):
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
                    find_ConflictoPagoSalario= ConflictoPagoSalarioModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_ConflictoPagoSalario)
                    data=find_ConflictoPagoSalario
                elif amount =='all':
                    all_ConflictoPagoSalario=ConflictoPagoSalarioModel.objects.all()
                    data=all_ConflictoPagoSalario

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of ConflictoPagoSalario:  ",error)
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


            try:

                montoDinero_PagoSalario = None
                fechaFinNoPagoSalario = None
                fechaInicioNoPagoSalario = None
                contrato = None
                demandaEmpresa = None
                demandaPersonaNatural = None

                if request.data['fechaInicioNoPagoSalario']!=None:
                    fechaInicioNoPagoSalario = request.data['fechaInicioNoPagoSalario']

                if request.data['fechaFinNoPagoSalario']!=None:
                    fechaFinNoPagoSalario = request.data['fechaFinNoPagoSalario']

                if request.data['montoDinero_PagoSalario']!=None:
                    montoDinero_PagoSalario = request.data['montoDinero_PagoSalario']


                if request.data['demandaPersonaNatural_id']!=None:
                    demandaPersonaNatural = DemandaPersonaNaturalModel.objects.get(id=request.data['demandaPersonaNatural_id'])

                if request.data['demandaEmpresa_id']!=None:
                    demandaEmpresa = DemandaEmpresaModel.objects.get(id=request.data['demandaEmpresa_id'])

                if request.data['contrato_id']!=None:
                    contrato = ContratoLaboralModel.objects.get(id=request.data['contrato_id'])




                ConflictoPagoSalario_obj=ConflictoPagoSalarioModel.objects.create(

                                                                        montoDinero_PagoSalario = montoDinero_PagoSalario,
                                                                        fechaFinNoPagoSalario = fechaFinNoPagoSalario,
                                                                        fechaInicioNoPagoSalario = fechaInicioNoPagoSalario,
                                                                        contrato = contrato,
                                                                        demandaEmpresa = demandaEmpresa,
                                                                        demandaPersonaNatural = demandaPersonaNatural,
              )


                status=200
                response['result']=True
                response['data']={
                    'id_ConflictoPagoSalario_obj':ConflictoPagoSalario_obj.id
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


                ConflictoPagoSalario_obj=ConflictoPagoSalarioModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(ConflictoPagoSalario_obj)

                status=200
                response['result']=True
                response['detail']='Actualización realizada con éxito'

            except Exception as error:
                print('error in update process:', error)
                response['detail']=f'{str(error)}'


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
                ConflictoPagoSalario_obj=ConflictoPagoSalarioModel.objects.filter(id=int(request.query_params.get('id')))

                if len(ConflictoPagoSalario_obj)==0:
                    response['detail'] ='ConflictoPagoSalario no existe en laborapp'
                elif ConflictoPagoSalario_obj[0].is_active is False:
                    response['detail'] ='ConflictoPagoSalario ya se encuentra inactiva en laborapp'
                elif len(ConflictoPagoSalario_obj)==1 and ConflictoPagoSalario_obj[0].is_active is True:
                    ConflictoPagoSalario_obj[0].is_active=False
                    ConflictoPagoSalario_obj[0].save()
                    status=200

                    response['detail'] ='ConflictoPagoSalario fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', ConflictoPagoSalario_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
