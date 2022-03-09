

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from demandaPersonaNatural.models import DemandaPersonaNaturalModel

import json

#import models from another apps

from user_profile.models import Municipios
from persona.models import PersonModel
from persona_natural.models import PersonaNaturalModel
from contratoLaboral.models import ContratoLaboralModel


class DemandaPersonaNaturalViews(APIView):



        queryset = DemandaPersonaNaturalModel.objects.all()



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
                    find_demandaPersonaNatural= DemandaPersonaNaturalModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_demandaPersonaNatural)
                    data=find_demandaPersonaNatural
                elif amount =='all':
                    all_demandaPersonaNatural=DemandaPersonaNaturalModel.objects.all()
                    data=all_demandaPersonaNatural

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of demandaPersonaNatural:  ",error)
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

            informedesicionfinaldemandapersonan = None
            fecharrealradicacionderechopetipersonan = None
            fechademandapersonanatural = None
            fecharrealradicaciondemandapersonan = None
            fechapropuestaradicaciondemandapersonan = None
            respuestafinaldemandaersonan=None

            try:
                print("***  Exist informedesicionfinaldemandapersonan: ", request.data["informedesicionfinaldemandapersonan"])

                if request.data['ubicacion_id']!='None':
                    ubicacion = Municipios.objects.get(id_municipio=request.data['ubicacion_id'])
                if request.data['personaNatural_id']!='None':
                    personaNatural = PersonaNaturalModel.objects.get(idPersonaNatural =request.data['personaNatural_id'])
                if request.data['contrato_id']!='None':
                    contrato = ContratoLaboralModel.objects.get(id=request.data['contrato_id'])
                if request.data['demandante_id']!='None':
                    demandante = PersonModel.objects.get(id=request.data['demandante_id'])

                if request.data["informedesicionfinaldemandapersonan"]!=None:
                    informedesicionfinaldemandapersonan=request.data["informedesicionfinaldemandapersonan"]
                    print("***  =( Exist informedesicionfinaldemandapersonan: ", request.data["informedesicionfinaldemandapersonan"])
                    print("***  =( Exist informedesicionfinaldemandapersonan: ", informedesicionfinaldemandapersonan)

                if request.data["fecharrealradicacionderechopetipersonan"]!=None:
                    fecharrealradicacionderechopetipersonan=request.data["fecharrealradicacionderechopetipersonan"]
                    print("***  Exist fecharrealradicacionderechopetipersonan ")

                if request.data["fechademandapersonanatural"]!=None:
                    fechademandapersonanatural=request.data["fechademandapersonanatural"]
                    print("***  Exist fechademandapersonanatural")

                if request.data["fecharrealradicaciondemandapersonan"]!=None:
                    fecharrealradicaciondemandapersonan=request.data["fecharrealradicaciondemandapersonan"]
                    print("***  Exist fecharrealradicaciondemandapersonan")

                if request.data["fechapropuestaradicaciondemandapersonan"]!=None:
                    fechapropuestaradicaciondemandapersonan=request.data["fechapropuestaradicaciondemandapersonan"]
                    print("***  Exist fechapropuestaradicaciondemandapersonan")

                if request.data["respuestafinaldemandaersonan"]!=None:
                    respuestafinaldemandaersonan=request.data["respuestafinaldemandaersonan"]
                    print("***  Exist respuestafinaldemandaersonan")

                print("**informedesicionfinaldemandapersonan: ", informedesicionfinaldemandapersonan)






                demandaPersonaNatural_obj=DemandaPersonaNaturalModel.objects.create(
                superaminimacuantiapersnat = request.data["superaminimacuantiapersnat"],
                    montototaldemandapersnat = request.data["montototaldemandapersnat"],
                    respuestafinaldemandaersonan=respuestafinaldemandaersonan,
                    informedesicionfinaldemandapersonan=informedesicionfinaldemandapersonan,
                                    fecharrealradicacionderechopetipersonan=fecharrealradicacionderechopetipersonan,
                                    fechademandapersonanatural=fechademandapersonanatural,
                                    fecharrealradicaciondemandapersonan=fecharrealradicaciondemandapersonan,
                                    fechapropuestaradicaciondemandapersonan=fechapropuestaradicaciondemandapersonan,
                                    contrato = contrato,
                                    personanatural = personaNatural,
                                    ubicacion = ubicacion,
                                    demandante=demandante
              )


                status=200
                response['result']=True
                response['data']={
                    'id_demandaPersonaNatural_obj':demandaPersonaNatural_obj.id
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


                demandaPersonaNatural_obj=DemandaPersonaNaturalModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(demandaPersonaNatural_obj)

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
                demandaPersonaNatural_obj=DemandaPersonaNaturalModel.objects.filter(id=int(request.query_params.get('id')))

                if len(demandaPersonaNatural_obj)==0:
                    response['detail'] ='demandaPersonaNatural no existe en laborapp'
                elif demandaPersonaNatural_obj[0].is_active is False:
                    response['detail'] ='demandaPersonaNatural ya se encuentra inactiva en laborapp'
                elif len(demandaPersonaNatural_obj)==1 and demandaPersonaNatural_obj[0].is_active is True:
                    demandaPersonaNatural_obj[0].is_active=False
                    demandaPersonaNatural_obj[0].save()
                    status=200

                    response['detail'] ='demandaPersonaNatural fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', demandaPersonaNatural_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
