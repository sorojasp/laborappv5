

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from user_profile.models import User_profileModel

import json

#import models from another apps





class User_profileViews(APIView):



        queryset = User_profileModel.objects.all()



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
                    find_user_profile= User_profileModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_user_profile)
                    data=find_user_profile
                elif amount =='all':
                    all_user_profile=User_profileModel.objects.all()
                    data=all_user_profile

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of user_profile:  ",error)
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


                user_profile_obj=User_profileModel.objects.create(
                      password = request.data["password"],
                                    email = request.data["email"],
              )


                status=200
                response['result']=True
                response['data']={
                    'id_user_profile_obj':user_profile_obj.id
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


                user_profile_obj=User_profileModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(user_profile_obj)

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
                user_profile_obj=user_profileModel.objects.filter(id=int(request.query_params.get('id')))

                if len(user_profile_obj)==0:
                    response['detail'] ='user_profile no existe en laborapp'
                elif user_profile_obj[0].is_active is False:
                    response['detail'] ='user_profile ya se encuentra inactiva en laborapp'
                elif len(user_profile_obj)==1 and user_profile_obj[0].is_active is True:
                    user_profile_obj[0].is_active=False
                    user_profile_obj[0].save()
                    status=200

                    response['detail'] ='user_profile fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', user_profile_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
