

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from conflictoCesantias.models import ConflictoCesantiasModel

import json

#import models from another apps

from demandaEmpresa.models import DemandaEmpresaModel
from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from contratoLaboral.models import ContratoLaboralModel




class ConflictoCesantiasViews(APIView):



        queryset = ConflictoCesantiasModel.objects.all()



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
                    find_ConflictoCesantias= ConflictoCesantiasModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_ConflictoCesantias)
                    data=find_ConflictoCesantias
                elif amount =='all':
                    all_ConflictoCesantias=ConflictoCesantiasModel.objects.all()
                    data=all_ConflictoCesantias

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of ConflictoCesantias:  ",error)
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


                desdeCuandoNoPaganCesantias = None
                fechaFinalNoPagoCesantias = None
                fechaUltimasCesantiasPagadas = None
                cantidadesPorAnio = None
                anios = None
                montoDinero_Cesantias = None
                contrato = None
                demandaEmpresa = None
                demandaPersonaNatural = None



                if request.data['montoDinero_Cesantias']!=None:
                    montoDinero_Cesantias = request.data['montoDinero_Cesantias']

                if request.data['anios']!=None:
                    anios = request.data['anios']

                if request.data['cantidadesPorAnio']!=None:
                    cantidadesPorAnio = request.data['cantidadesPorAnio']

                if request.data['fechaUltimasCesantiasPagadas']!=None:
                    fechaUltimasCesantiasPagadas = request.data['fechaUltimasCesantiasPagadas']

                if request.data['fechaFinalNoPagoCesantias']!=None:
                    fechaFinalNoPagoCesantias = request.data['fechaFinalNoPagoCesantias']

                if request.data['desdeCuandoNoPaganCesantias']!=None:
                    desdeCuandoNoPaganCesantias = request.data['desdeCuandoNoPaganCesantias']

                if request.data['demandaPersonaNatural_id']!=None:
                    demandaPersonaNatural = DemandaPersonaNaturalModel.objects.get(id=request.data['demandaPersonaNatural_id'])

                if request.data['demandaEmpresa_id']!=None:
                    demandaEmpresa = DemandaEmpresaModel.objects.get(id=request.data['demandaEmpresa_id'])

                if request.data['contrato_id']!=None:
                    contrato = ContratoLaboralModel.objects.get(id=request.data['contrato_id'])


                ConflictoCesantias_obj=ConflictoCesantiasModel.objects.create(

                                                                        desdeCuandoNoPaganCesantias = desdeCuandoNoPaganCesantias,
                                                                        fechaFinalNoPagoCesantias = fechaFinalNoPagoCesantias,
                                                                        fechaUltimasCesantiasPagadas = fechaUltimasCesantiasPagadas,
                                                                        cantidadesPorAnio = cantidadesPorAnio,
                                                                        anios = anios,
                                                                        montoDinero_Cesantias = montoDinero_Cesantias,
              )


                status=200
                response['result']=True
                response['data']={
                    'id_ConflictoCesantias_obj':ConflictoCesantias_obj.id
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


                ConflictoCesantias_obj=ConflictoCesantiasModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(ConflictoCesantias_obj)

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
                ConflictoCesantias_obj=ConflictoCesantiasModel.objects.filter(id=int(request.query_params.get('id')))

                if len(ConflictoCesantias_obj)==0:
                    response['detail'] ='ConflictoCesantias no existe en laborapp'
                elif ConflictoCesantias_obj[0].is_active is False:
                    response['detail'] ='ConflictoCesantias ya se encuentra inactiva en laborapp'
                elif len(ConflictoCesantias_obj)==1 and ConflictoCesantias_obj[0].is_active is True:
                    ConflictoCesantias_obj[0].is_active=False
                    ConflictoCesantias_obj[0].save()
                    status=200

                    response['detail'] ='ConflictoCesantias fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', ConflictoCesantias_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
