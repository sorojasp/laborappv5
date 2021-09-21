from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user_profile import models
from django.db.utils import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status

# Create your views here.


class UserProfile(APIView):
    
    
    
    
    
    
    def get (self, request,format=None, pk=None):
        
        status=200
        amount=request.query_params.get('amount')
        
        if amount =='one':
            find_user=models.UserProfile.objects.get(id=int(request.query_params.get('id')))
            print(find_user)
        elif amount =='all':
            pass
        
        print(request.query_params.get("amount"))
        return Response({"name":"Stiven Rojas",
                         'pk': pk},status=200)
    
    
    
    def post(self,request,format=None,pk=None):
        status=200
        
        response={
            'result':None,
            'data':None,
            'detail':None
            }
        
        try:
            user=models.UserProfile.objects.create(email=request.data['email'],
                                                   password=request.data['password'])
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            
            response['result']=True
            response['detail']='Usuario creado exitosamente'
            response['data']={
                'user_id':user.id,
                'user_email':user.email,
                'token':str(token)
            }
        except IntegrityError:
            response['result']=False
            response['detail']='correo ya existe en laborapp'
            status=500
            
        return Response(response,status=status) 
            
    
    