

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from conflictoContactaAbogado.models import ConflictoContactaAbogadoModel

import json

#import models from another apps


from demandaPersonaNatural.models import DemandaPersonaNaturalModel
from demandaEmpresa.models import DemandaEmpresaModel





class ConflictoContactaAbogadoViews(APIView):



        queryset = ConflictoContactaAbogadoModel.objects.all()



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
                    find_conflictoContactaAbogado= ConflictoContactaAbogadoModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_conflictoContactaAbogado)
                    data=find_conflictoContactaAbogado
                elif amount =='all':
                    all_conflictoContactaAbogado=ConflictoContactaAbogadoModel.objects.all()
                    data=all_conflictoContactaAbogado

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of conflictoContactaAbogado:  ",error)
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


                demandaEmpresa = None
                demandaPersonaNatural = None
                conflictoDominicalesFestivos = None
                conflictoHorasExtras = None
                conflictoPensiones = None
                conflictoARL = None

                if request.data['conflictoARL']!=None:
                    conflictoARL = request.data['conflictoARL']

                if request.data['conflictoPensiones']!=None:
                    conflictoPensiones = request.data['conflictoPensiones']

                if request.data['conflictoHorasExtras']!=None:
                    conflictoHorasExtras = request.data['conflictoHorasExtras']

                if request.data['conflictoDominicalesFestivos']!=None:
                    conflictoDominicalesFestivos = request.data['conflictoDominicalesFestivos']

                if request.data['demandaPersonaNatural_id']!=None:
                    demandaPersonaNatural = DemandaPersonaNaturalModel.objects.get(id=request.data['demandaPersonaNatural_id'])

                if request.data['demandaEmpresa_id']!=None:
                    demandaEmpresa = DemandaEmpresaModel.objects.get(id=request.data['demandaEmpresa_id'])


                conflictoContactaAbogado_obj=ConflictoContactaAbogadoModel.objects.create(

                                                                        demandaEmpresa = demandaEmpresa,
                                                                        demandaPersonaNatural = demandaPersonaNatural,
                                                                        conflictoDominicalesFestivos = conflictoDominicalesFestivos,
                                                                        conflictoHorasExtras = conflictoHorasExtras,
                                                                        conflictoPensiones = conflictoPensiones,
                                                                        conflictoARL = conflictoARL,
              )


                status=200
                response['result']=True
                response['data']={
                    'id_conflictoContactaAbogado_obj':conflictoContactaAbogado_obj.id
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


                conflictoContactaAbogado_obj=ConflictoContactaAbogadoModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(conflictoContactaAbogado_obj)

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
                conflictoContactaAbogado_obj=ConflictoContactaAbogadoModel.objects.filter(id=int(request.query_params.get('id')))

                if len(conflictoContactaAbogado_obj)==0:
                    response['detail'] ='conflictoContactaAbogado no existe en laborapp'
                elif conflictoContactaAbogado_obj[0].is_active is False:
                    response['detail'] ='conflictoContactaAbogado ya se encuentra inactiva en laborapp'
                elif len(conflictoContactaAbogado_obj)==1 and conflictoContactaAbogado_obj[0].is_active is True:
                    conflictoContactaAbogado_obj[0].is_active=False
                    conflictoContactaAbogado_obj[0].save()
                    status=200

                    response['detail'] ='conflictoContactaAbogado fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', conflictoContactaAbogado_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
