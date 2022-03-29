

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from conflictoDespidoSJC.models import ConflictoDespidoSJCModel

import json

#import models from another apps




from demandaEmpresa.models import DemandaEmpresaModel
from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from contratoLaboral.models import ContratoLaboralModel


class ConflictoDespidoSJCViews(APIView):



        queryset = ConflictoDespidoSJCModel.objects.all()



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
                    find_conflicto_despidoSJC= ConflictoDespidoSJCModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_conflicto_despidoSJC)
                    data=find_conflicto_despidoSJC
                elif amount =='all':
                    all_conflicto_despidoSJC=ConflictoDespidoSJCModel.objects.all()
                    data=all_conflicto_despidoSJC

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of conflicto_despidoSJC:  ",error)
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



                montoDinero_DSJC = None
                fechaDespido = None
                contrato = None
                tipoContrato = None
                fechaInicioContrato = None
                demandaEmpresa = None
                demandaPersonaNatural = None
                if request.data['fechaInicioContrato']!=None:
                    fechaInicioContrato = request.data['fechaInicioContrato']

                if request.data['tipoContrato']!=None:
                    tipoContrato = request.data['tipoContrato']

                if request.data['fechaDespido']!=None:
                    fechaDespido = request.data['fechaDespido']

                if request.data['montoDinero_DSJC']!=None:
                    montoDinero_DSJC = request.data['montoDinero_DSJC']


                if request.data['idDemandaPersonaNatural_id']!=None:
                    demandaPersonaNatural = DemandaPersonaNaturalModel.objects.get(id=request.data['idDemandaPersonaNatural_id'])


                if request.data['idDemandaEmpresa_id']!=None:


                    demandaEmpresa = DemandaEmpresaModel.objects.get(id=request.data['idDemandaEmpresa_id'])
                    print("demandaEmpresa", demandaEmpresa)

                if request.data['idContrato_id']!=None:
                    contrato = ContratoLaboralModel.objects.get(id=request.data['idContrato_id'])



                conflicto_despidoSJC_obj=ConflictoDespidoSJCModel.objects.create(

                                                                        montoDinero_DSJC = montoDinero_DSJC,
                                                                        fechaDespido = fechaDespido,
                                                                        contrato = contrato,
                                                                        tipoContrato = tipoContrato,
                                                                        fechaInicioContrato = fechaInicioContrato,
                                                                        demandaEmpresa = demandaEmpresa,
                                                                        demandaPersonaNatural = demandaPersonaNatural,
              )


                status=200
                response['result']=True
                response['data']={
                    'id_conflicto_despidoSJC_obj':conflicto_despidoSJC_obj.id
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


                conflicto_despidoSJC_obj=ConflictoDespidoSJCModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(conflicto_despidoSJC_obj)

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
                conflicto_despidoSJC_obj=ConflictoDespidoSJCModel.objects.filter(id=int(request.query_params.get('id')))

                if len(conflicto_despidoSJC_obj)==0:
                    response['detail'] ='conflicto_despidoSJC no existe en laborapp'
                elif conflicto_despidoSJC_obj[0].is_active is False:
                    response['detail'] ='conflicto_despidoSJC ya se encuentra inactiva en laborapp'
                elif len(conflicto_despidoSJC_obj)==1 and conflicto_despidoSJC_obj[0].is_active is True:
                    conflicto_despidoSJC_obj[0].is_active=False
                    conflicto_despidoSJC_obj[0].save()
                    status=200

                    response['detail'] ='conflicto_despidoSJC fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', conflicto_despidoSJC_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
