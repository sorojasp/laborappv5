from django.shortcuts import render
from rest_framework.views import APIView
from persona_natural import models as persona_natural_models

from rest_framework.response import Response
from persona import models as persona_models

# Create your views here.
import json
from django.core import serializers

class PersonaNatural(APIView):

    def get(self, request, *args, **kwargs):
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
                find_person_natural=persona_natural_models.PersonaNaturalModel.objects.filter(idPersonaNatural=int(request.query_params.get('id')))
                print(find_person_natural)
                data=find_person_natural
            elif amount =='all':
                all_person_natural=persona_natural_models.PersonaNaturalModel.objects.all()
                data=all_person_natural

            response['data']=json.loads(serializers.serialize('json', data))
            response['result']=True
            response['detail']= "consulta exitosa"
            status=200
        except Exception as error:
            print("** error in get of person:  ",error)
            response['result']=False
            response['detail']= str(error)
            status=500

        return Response({"data":response,
                        },status=status)


    def post(self, request, *args, **kwargs):

        status=500
        print("here ....")

        response={
            'result':False,
            'data':None,
            'detail':None
            }

        user=None
        person=None


        try:
            if request.data['persona_id']!='None':
                person = persona_models.PersonModel.objects.get(id=request.data['persona_id'])

            person_natural_obj=persona_natural_models.PersonaNaturalModel.objects.create(
            person=person,
            )


            status=200
            response['result']=True
            response['data']={
                'id_person_natural':person_natural_obj.idPersonaNatural
            }
        except Exception as e:
            response['details']=str(e)

        return Response(response,status=status)


    def patch(self,request,format=None,pk=None):

        status=200

        response={
            'result':False,
            'data':None,
            'detail':'Not implemented yet. Please use the person service'
            }



        return Response(response,status=status)


    def delete(self,request,format=None,pk=None):
        status=200

        response={
            'result':False,
            'data':None,
            'detail':'Not implemented yet. Please use the person service'
            }

        return Response(response,status=status)
