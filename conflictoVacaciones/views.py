

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from conflictoVacaciones.models import ConflictoPagoVacaciones

from demandaEmpresa.models import DemandaEmpresaModel
from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from contratoLaboral.models import ContratoLaboralModel

import json

#import models from another apps






class ConflictoPagoVacacionesViews(APIView):



        queryset = ConflictoPagoVacaciones.objects.all()



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
                    find_ConflictoPagoVacaciones= ConflictoPagoVacaciones.objects.filter(id=int(request.query_params.get('id')))
                    print(find_ConflictoPagoVacaciones)
                    data=find_ConflictoPagoVacaciones
                elif amount =='all':
                    all_ConflictoPagoVacaciones=ConflictoPagoVacaciones.objects.all()
                    data=all_ConflictoPagoVacaciones

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of ConflictoPagoVacaciones:  ",error)
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


                desdeCuandoNoPaganVacaciones = None
                fechaFinalCalculoVacaciones = None
                fechaInicioCalculoVacaciones = None
                montoDinero_Vacaciones = None
                contrato = None
                demandaEmpresa = None
                demandaPersonaNatural = None

                if request.data['montoDinero_Vacaciones']!=None:
                    montoDinero_Vacaciones = request.data['montoDinero_Vacaciones']

                if request.data['fechaInicioCalculoVacaciones']!=None:
                    fechaInicioCalculoVacaciones = request.data['fechaInicioCalculoVacaciones']

                if request.data['fechaFinalCalculoVacaciones']!=None:
                    fechaFinalCalculoVacaciones = request.data['fechaFinalCalculoVacaciones']

                if request.data['desdeCuandoNoPaganVacaciones']!=None:
                    desdeCuandoNoPaganVacaciones = request.data['desdeCuandoNoPaganVacaciones']

                if request.data['demandaPersonaNatural_id']!=None:
                    demandaPersonaNatural = DemandaPersonaNaturalModel.objects.get(id=request.data['demandaPersonaNatural_id'])

                if request.data['demandaEmpresa_id']!=None:
                    demandaEmpresa = DemandaEmpresaModel.objects.get(id=request.data['demandaEmpresa_id'])

                if request.data['contrato_id']!=None:
                    contrato = ContratoLaboralModel.objects.get(id=request.data['contrato_id'])




                ConflictoPagoVacaciones_obj=ConflictoPagoVacaciones.objects.create(

                                                                        desdeCuandoNoPaganVacaciones = desdeCuandoNoPaganVacaciones,
                                                                        fechaFinalCalculoVacaciones = fechaFinalCalculoVacaciones,
                                                                        fechaInicioCalculoVacaciones = fechaInicioCalculoVacaciones,
                                                                        montoDinero_Vacaciones = montoDinero_Vacaciones,
                                                                        contrato = contrato,
                                                                        demandaEmpresa = demandaEmpresa,
                                                                        demandaPersonaNatural = demandaPersonaNatural
              )


                status=200
                response['result']=True
                response['data']={
                    'id_ConflictoPagoVacaciones_obj':ConflictoPagoVacaciones_obj.id
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


                ConflictoPagoVacaciones_obj=ConflictoPagoVacaciones.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(ConflictoPagoVacaciones_obj)

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
                ConflictoPagoVacaciones_obj=ConflictoPagoVacaciones.objects.filter(id=int(request.query_params.get('id')))

                if len(ConflictoPagoVacaciones_obj)==0:
                    response['detail'] ='ConflictoPagoVacaciones no existe en laborapp'
                elif ConflictoPagoVacaciones_obj[0].is_active is False:
                    response['detail'] ='ConflictoPagoVacaciones ya se encuentra inactiva en laborapp'
                elif len(ConflictoPagoVacaciones_obj)==1 and ConflictoPagoVacaciones_obj[0].is_active is True:
                    ConflictoPagoVacaciones_obj[0].is_active=False
                    ConflictoPagoVacaciones_obj[0].save()
                    status=200

                    response['detail'] ='ConflictoPagoVacaciones fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', ConflictoPagoVacaciones_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
