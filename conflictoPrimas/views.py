

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from conflictoPrimas.models import ConflictoPrimasModel

import json

#import models from another apps

from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from demandaEmpresa.models import DemandaEmpresaModel
from contratoLaboral.models import ContratoLaboralModel





class ConflictoPrimasViews(APIView):



        queryset = ConflictoPrimasModel.objects.all()



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
                    find_conflictoPrimas= ConflictoPrimasModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_conflictoPrimas)
                    data=find_conflictoPrimas
                elif amount =='all':
                    all_conflictoPrimas=ConflictoPrimasModel.objects.all()
                    data=all_conflictoPrimas

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of conflictoPrimas:  ",error)
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


                contrato = None
                demandaEmpresa = None
                demandaPersonaNatural = None
                montoDinero_Prima = None
                fechaFinalNoPagoPrima = None
                fechaUltimaPrimaPagada = None

                if request.data['fechaUltimaPrimaPagada']!=None:
                    fechaUltimaPrimaPagada = request.data['fechaUltimaPrimaPagada']

                if request.data['fechaFinalNoPagoPrima']!=None:
                    fechaFinalNoPagoPrima = request.data['fechaFinalNoPagoPrima']

                if request.data['montoDinero_Prima']!=None:
                    montoDinero_Prima = request.data['montoDinero_Prima']

                if request.data['demandaPersonaNatural_id']!=None:
                    demandaPersonaNatural = DemandaPersonaNaturalModel.objects.get(id=request.data['demandaPersonaNatural_id'])

                if request.data['demandaEmpresa_id']!=None:
                    demandaEmpresa = DemandaEmpresaModel.objects.get(id=request.data['demandaEmpresa_id'])

                if request.data['contrato_id']!=None:
                    contrato = ContratoLaboralModel.objects.get(id=request.data['contrato_id'])




                conflictoPrimas_obj=ConflictoPrimasModel.objects.create(

                                                                        contrato = contrato,
                                                                        demandaEmpresa = demandaEmpresa,
                                                                        demandaPersonaNatural = demandaPersonaNatural,
                                                                        montoDinero_Prima = montoDinero_Prima,
                                                                        fechaFinalNoPagoPrima = fechaFinalNoPagoPrima,
                                                                        fechaUltimaPrimaPagada = fechaUltimaPrimaPagada,
              )


                status=200
                response['result']=True
                response['data']={
                    'id_conflictoPrimas_obj':conflictoPrimas_obj.id
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


                conflictoPrimas_obj=ConflictoPrimasModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(conflictoPrimas_obj)

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
                conflictoPrimas_obj=ConflictoPrimasModel.objects.filter(id=int(request.query_params.get('id')))


                if len(conflictoPrimas_obj)==0:
                    response['detail'] ='conflictoPrimas no existe en laborapp'
                elif conflictoPrimas_obj[0].is_active is False:
                    response['detail'] ='conflictoPrimas ya se encuentra inactiva en laborapp'
                elif len(conflictoPrimas_obj)==1 and conflictoPrimas_obj[0].is_active is True:
                    conflictoPrimas_obj[0].is_active=False
                    conflictoPrimas_obj[0].save()
                    status=200

                    response['detail'] ='conflictoPrimas fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', conflictoPrimas_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
