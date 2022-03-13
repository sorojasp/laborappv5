

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from conflictoLiquidacion.models import ConflictoLiquidacionModel

import json

#import models from another apps

from demandaEmpresa.models import DemandaEmpresaModel
from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from contratoLaboral.models import ContratoLaboralModel




class ConflictoLiquidacionViews(APIView):



        queryset = ConflictoLiquidacionModel.objects.all()



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
                    find_ConflictoLiquidacion= ConflictoLiquidacionModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_ConflictoLiquidacion)
                    data=find_ConflictoLiquidacion
                elif amount =='all':
                    all_ConflictoLiquidacion=ConflictoLiquidacionModel.objects.all()
                    data=all_ConflictoLiquidacion

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of ConflictoLiquidacion:  ",error)
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


                fechaInicioLiquidacion = None
                fechaFinalLiquidacion = None
                montoDinero_Vacaciones = None
                montoDinero_Prima = None
                diasDeVacaciones = None
                contrato = None
                demandaEmpresa = None
                demandaPersonaNatural = None


                if request.data['diasDeVacaciones']!=None:
                    diasDeVacaciones = request.data['diasDeVacaciones']

                if request.data['montoDinero_Prima']!=None:
                    montoDinero_Prima = request.data['montoDinero_Prima']

                if request.data['montoDinero_Vacaciones']!=None:
                    montoDinero_Vacaciones = request.data['montoDinero_Vacaciones']

                if request.data['fechaFinalLiquidacion']!=None:
                    fechaFinalLiquidacion = request.data['fechaFinalLiquidacion']

                if request.data['fechaInicioLiquidacion']!=None:
                    fechaInicioLiquidacion = request.data['fechaInicioLiquidacion']

                if request.data['demandaPersonaNatural_id']!=None:
                    demandaPersonaNatural = DemandaPersonaNaturalModel.objects.get(id=request.data['demandaPersonaNatural_id'])

                if request.data['demandaEmpresa_id']!=None:
                    demandaEmpresa = DemandaEmpresaModel.objects.get(id=request.data['demandaEmpresa_id'])

                if request.data['contrato_id']!=None:
                    contrato = ContratoLaboralModel.objects.get(id=request.data['contrato_id'])


                ConflictoLiquidacion_obj=ConflictoLiquidacionModel.objects.create(

                                                                        fechaInicioLiquidacion = fechaInicioLiquidacion,
                                                                        fechaFinalLiquidacion = fechaFinalLiquidacion,
                                                                        montoDinero_Vacaciones = montoDinero_Vacaciones,
                                                                        montoDinero_Prima = montoDinero_Prima,
                                                                        diasDeVacaciones = diasDeVacaciones,
                                                                        contrato = contrato,
                                                                        demandaEmpresa = demandaEmpresa,
                                                                        demandaPersonaNatural = demandaPersonaNatural
              )


                status=200
                response['result']=True
                response['data']={
                    'id_ConflictoLiquidacion_obj':ConflictoLiquidacion_obj.id
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


                ConflictoLiquidacion_obj=ConflictoLiquidacionModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(ConflictoLiquidacion_obj)

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
                ConflictoLiquidacion_obj=ConflictoLiquidacionModel.objects.filter(id=int(request.query_params.get('id')))

                if len(ConflictoLiquidacion_obj)==0:
                    response['detail'] ='ConflictoLiquidacion no existe en laborapp'
                elif ConflictoLiquidacion_obj[0].is_active is False:
                    response['detail'] ='ConflictoLiquidacion ya se encuentra inactiva en laborapp'
                elif len(ConflictoLiquidacion_obj)==1 and ConflictoLiquidacion_obj[0].is_active is True:
                    ConflictoLiquidacion_obj[0].is_active=False
                    ConflictoLiquidacion_obj[0].save()
                    status=200

                    response['detail'] ='ConflictoLiquidacion fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', ConflictoLiquidacion_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
