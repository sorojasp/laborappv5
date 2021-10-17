import re
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user_profile import models
from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.core import serializers
import json

from utils.encrypt.encrypt import Encrypt
from utils.sender_email.EnviadorCorreos import EnviadorCorreos


import yagmail



# Create your views here.


class UserProfile(APIView):

    def get (self, request,format=None, pk=None):

        print("u are reach the get....")
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
                find_user=models.UserProfile.objects.filter(id=int(request.query_params.get('id')))
                data=find_user
            elif amount =='all':
                all_user=models.UserProfile.objects.all()
                data=all_user

            response['data']=json.loads(serializers.serialize('json', data))
            response['result']=True
            response['detail']= "consulta exitosa"
            status=200
        except Exception as error:
            print(error)
            response['result']=False
            response['detail']= str(error)
            status=500




        return Response({"data":response,
                        },status=status)

    def post(self,request,format=None,pk=None):
        encrypt=Encrypt()
        enviador_correos:EnviadorCorreos=EnviadorCorreos()

        status=500

        response={
            'result':False,
            'data':None,
            'detail':None
            }


        yagmail.register("recyappbeta1@gmail.com", "#Stiven1911")

        receiver = request.data['email']
        body = "Hello there from Yagmail"
        filename = "demanda.pdf"

        yag = yagmail.SMTP("recyappbeta1@gmail.com")
        yag.send(
            to=receiver,
            subject="Yagmail test with attachment",
            contents=body,
            attachments=filename,
        )


        try:

            password_encrypted:str=encrypt.encrypt_msg(request.data['password'])
            user=models.UserProfile.objects.create(email=request.data['email'],
                                                   password=password_encrypted)


            user.save()
            token, created = Token.objects.get_or_create(user=user)

            response['result']=True
            response['detail']='Usuario creado exitosamente'
            response['data']={
                'user_id':user.id,
                'user_email':user.email,
                'token':str(token)
            }
            enviador_correos.sendEmail(request.data['email'],"Bienvenido a laborapp","Cordial saludo",
                                       "Es un gran placer poderlos ayudar en la adversidad, sepán que estamos para servir al pueblo.")

            status=200
        except IntegrityError:
            response['detail']='correo ya existe en laborapp'
        except Exception as error:
            response['detail']=str(error)


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

            id=str(request.query_params.get('id'))

            userProfile_obj=models.UserProfile.objects.update_or_create(id=request.query_params.get('id'),
                                                                        defaults=request.data)

            print(userProfile_obj)

            response['result']=True
            response['detail']='Actualización realizada con éxito'

        except Exception as error:
            print("error in update process:", error)
            response['detail']=str(error)



        return Response(response,200)


    def delete(self,request,format=None,pk=None):

        status=500

        response={
            'result':False,
            'data':None,
            'detail':None
            }

        try:
            id=request.query_params.get('id')
            obj_user=models.UserProfile.objects.filter(id=int(request.query_params.get('id')))

            if len(obj_user)==0:
                response['detail'] ="Usuario no existe en laborapp"
            elif obj_user[0].is_active is False:
                response['detail'] ="Usuario ya se encuentra inactivo en laborapp"
            elif len(obj_user)==1 and obj_user[0].is_active is True:
                obj_user[0].is_active=False
                obj_user[0].save()
                status=200

                response['detail'] ="El usuario fue dado de baja con éxito"
                response['result']=True
                response['data']=json.loads(serializers.serialize('json', obj_user))

        except Exception as error:
            response['detail'] = f"error:{str(error)}"


        return Response({"data":response,},status=status)


class UserLogin(APIView):

    def get(self,request,format=None,pk=None):

        status=500

        response={
            'result':False,
            'data':None,
            'detail':None
            }

        encrypt:Encrypt=Encrypt()
        password_encrypted=encrypt.encrypt_msg(request.data['password'])


        try:
            user_obj=models.UserProfile.objects.filter(email=request.data['email'],
                                                   password=password_encrypted)

            if len(user_obj)==0:
                response['result'] = False
                response['detail']='Usuario no existe en laborapp'
            else:
                response['result'] = True
                response['detail']='Usuario logeado con éxito'
                response['data'] = json.loads(serializers.serialize('json', user_obj))


        except Exception as error:
            response['result'] = False
            response['detail']=str(error)



        return Response({'data':response},status)


class Departamentos(APIView):


    def get(self, request,format=None,pk=None):

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
                find_deparment=models.Departamentos.objects.filter( id_departamento=request.query_params.get('id'))
                data=find_deparment
            elif amount =='all':
                all_deparments=models.Departamentos.objects.all()
                data=all_deparments

            response['data']=json.loads(serializers.serialize('json', data))
            response['result']=True
            response['detail']= "consulta exitosa"
            status=200
        except Exception as error:
            print(error)
            response['result']=False
            response['detail']= str(error)
            status=500


        return Response({'data':response}, status=status)


class Municipios(APIView):



    def get(self, request,format=None,pk=None):

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
                find_municipios=models.Municipios.objects.filter( id_municipio=request.query_params.get('id'))
                data=find_municipios

            elif amount =='all':

                obj_deparment = models.Departamentos.objects.get(id_departamento=request.query_params.get('id'))
                all_municipios=models.Municipios.objects.filter(departamento_id = obj_deparment )
                data=all_municipios

            response['data']=json.loads(serializers.serialize('json', data))
            response['result']=True
            response['detail']= "consulta exitosa"
            status=200
        except Exception as error:
            print(error)
            response['result']=False
            response['detail']= str(error)
            status=500


        return Response({'data':response}, status=status)
