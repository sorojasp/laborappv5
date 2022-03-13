

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from ConflictoPrima.models import ConflictoPrimaModel

import json

#import models from another apps

from is_active.models import Is_activeModel




class ConflictoPrimaViews(APIView):



        queryset = ConflictoPrimaModel.objects.all()

        

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
                    find_ConflictoPrima= ConflictoPrimaModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_ConflictoPrima)
                    data=find_ConflictoPrima
                elif amount =='all':
                    all_ConflictoPrima=ConflictoPrimaModel.objects.all()
                    data=all_ConflictoPrima

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of ConflictoPrima:  ",error)
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

                                is_active = None
                id = None
                fechaFinalNoPagoPrima = None
                fechaUltimaPrimaPagada = None
                montoDinero_Prima = None
                if request.data['montoDinero_Prima']!=None:
                    montoDinero_Prima = request.data['montoDinero_Prima_id']

                if request.data['fechaUltimaPrimaPagada']!=None:
                    fechaUltimaPrimaPagada = request.data['fechaUltimaPrimaPagada_id']

                if request.data['fechaFinalNoPagoPrima']!=None:
                    fechaFinalNoPagoPrima = request.data['fechaFinalNoPagoPrima_id']

                if request.data['id']!=None:
                    id = request.data['id_id']

                if request.data['is_active_id']!=None:
                    is_active = BooleanModel.objects.get(id=request.data['is_active_id'])


                ConflictoPrima_obj=ConflictoPrimaModel.objects.create(
                                                          is_active = is_active,
                                                                        id = id,
                                                                        fechaFinalNoPagoPrima = fechaFinalNoPagoPrima,
                                                                        fechaUltimaPrimaPagada = fechaUltimaPrimaPagada,
                                                                        montoDinero_Prima = montoDinero_Prima,
              )


                status=200
                response['result']=True
                response['data']={
                    'id_ConflictoPrima_obj':ConflictoPrima_obj.id
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


                ConflictoPrima_obj=ConflictoPrimaModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(ConflictoPrima_obj)

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
                ConflictoPrima_obj=ConflictoPrimaModel.objects.filter(id=int(request.query_params.get('id')))

                if len(ConflictoPrima_obj)==0:
                    response['detail'] ='ConflictoPrima no existe en laborapp'
                elif ConflictoPrima_obj[0].is_active is False:
                    response['detail'] ='ConflictoPrima ya se encuentra inactiva en laborapp'
                elif len(ConflictoPrima_obj)==1 and ConflictoPrima_obj[0].is_active is True:
                    ConflictoPrima_obj[0].is_active=False
                    ConflictoPrima_obj[0].save()
                    status=200

                    response['detail'] ='ConflictoPrima fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', ConflictoPrima_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)






        