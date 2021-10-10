from django.shortcuts import render



from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from empresa.models import EmpresaModel
from user_profile.models import Municipios


# import contrtoLaboral model

from contratoLaboral.models import ContratoLaboralModel

# import models from another modules
from persona.models import PersonModel
from persona_natural.models import PersonaNaturalModel
from empresa.models import EmpresaModel

import json
# Create your views here.


class ContratoLaboralView(APIView):


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
                find_contratoLaboral= ContratoLaboralModel.objects.filter(id=int(request.query_params.get('id')))
                print(find_ContratoLaboral)
                data=find_ContratoLaboral
            elif amount =='all':
                all_contratoLaboral=ContratoLaboralModel.objects.all()
                data=all_contratoLaboral

            response['data']=json.loads(serializers.serialize('json', data))
            response['result']=True
            response['detail']= "consulta exitosa"
            status=200
        except Exception as error:
            print("** error in get request  of contrato laboral:  ",error)
            response['result']=False
            response['detail']= str(error)
            status=500

        return Response({"data":response,
                        },status=status)
