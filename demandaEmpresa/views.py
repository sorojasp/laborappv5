

from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from demandaEmpresa.models import DemandaEmpresaModel
from empresa.models import EmpresaModel

import json

#import models from another apps



from user_profile.models import Municipios
from contratoLaboral.models import ContratoLaboralModel




class DemandaEmpresaViews(APIView):



        queryset = DemandaEmpresaModel.objects.all()



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
                    find_demanda_empresa= DemandaEmpresaModel.objects.filter(id=int(request.query_params.get('id')))
                    print(find_demanda_empresa)
                    data=find_demanda_empresa
                elif amount =='all':
                    all_demanda_empresa=DemandaEmpresaModel.objects.all()
                    data=all_demanda_empresa

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of demanda_empresa:  ",error)
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

                id = None
                superaMinimaCuantiaPersJuri = None
                montoTotalDemandaPersJuri = None
                respuestaFinalDemandaEmpresa = None
                informeDesicionFinalDemandaEmpresa = None
                fecharRealRadicacionDerechoPetiEmpresa = None
                fechaPropuestaRadicacionDerechoPetiEmpresa = None
                fecharRealRadicacionDemandaEmpresa = None
                fechaPropuestaRadicacionDemandaEmpresa = None
                idContrato = None
                NItEmpresa = None
                numeroDocumentoPersona = None
                tipoDocumentoPersona = None
                codigoCiudad = None
                fechaDemandaEmpresa = None

                if request.data['fechaDemandaEmpresa']!=None:
                    fechaDemandaEmpresa = request.data['fechaDemandaEmpresa']

                if request.data['tipoDocumentoPersona']!=None:
                    tipoDocumentoPersona = request.data['tipoDocumentoPersona']

                if request.data['numeroDocumentoPersona']!=None:
                    numeroDocumentoPersona = request.data['numeroDocumentoPersona']

                if request.data['NItEmpresa']!=None:


                    NItEmpresa = EmpresaModel.objects.filter(NItEmpresa=request.data['NItEmpresa'])[0]
                    print("enterprises: ", NItEmpresa)

                if request.data['fechaPropuestaRadicacionDemandaEmpresa']!=None:
                    fechaPropuestaRadicacionDemandaEmpresa = request.data['fechaPropuestaRadicacionDemandaEmpresa']

                if request.data['fecharRealRadicacionDemandaEmpresa']!=None:
                    fecharRealRadicacionDemandaEmpresa = request.data['fecharRealRadicacionDemandaEmpresa']

                if request.data['fechaPropuestaRadicacionDerechoPetiEmpresa']!=None:
                    fechaPropuestaRadicacionDerechoPetiEmpresa = request.data['fechaPropuestaRadicacionDerechoPetiEmpresa']

                if request.data['fecharRealRadicacionDerechoPetiEmpresa']!=None:
                    fecharRealRadicacionDerechoPetiEmpresa = request.data['fecharRealRadicacionDerechoPetiEmpresa']

                if request.data['informeDesicionFinalDemandaEmpresa']!=None:
                    informeDesicionFinalDemandaEmpresa = request.data['informeDesicionFinalDemandaEmpresa']

                if request.data['respuestaFinalDemandaEmpresa']!=None:
                    respuestaFinalDemandaEmpresa = request.data['respuestaFinalDemandaEmpresa']

                if request.data['montoTotalDemandaPersJuri']!=None:
                    montoTotalDemandaPersJuri = float(request.data['montoTotalDemandaPersJuri'])

                if request.data['superaMinimaCuantiaPersJuri']!=None:
                    superaMinimaCuantiaPersJuri = request.data['superaMinimaCuantiaPersJuri']


                if request.data['codigoCiudad']!=None:
                    codigoCiudad = Municipios.objects.get(id_municipio =request.data['codigoCiudad'])

                if request.data['idContrato_id']!=None:
                    idContrato = ContratoLaboralModel.objects.get(id=request.data['idContrato_id'])


                demanda_empresa_obj=DemandaEmpresaModel.objects.create(

                                                                        superaMinimaCuantiaPersJuri = superaMinimaCuantiaPersJuri,
                                                                        montoTotalDemandaPersJuri = montoTotalDemandaPersJuri,
                                                                        respuestaFinalDemandaEmpresa = respuestaFinalDemandaEmpresa,
                                                                        informeDesicionFinalDemandaEmpresa = informeDesicionFinalDemandaEmpresa,
                                                                        fecharRealRadicacionDerechoPetiEmpresa = fecharRealRadicacionDerechoPetiEmpresa,
                                                                        fechaPropuestaRadicacionDerechoPetiEmpresa = fechaPropuestaRadicacionDerechoPetiEmpresa,
                                                                        fecharRealRadicacionDemandaEmpresa = fecharRealRadicacionDemandaEmpresa,
                                                                        fechaPropuestaRadicacionDemandaEmpresa = fechaPropuestaRadicacionDemandaEmpresa,
                                                                        idContrato = idContrato,
                                                                        NItEmpresa = NItEmpresa,
                                                                        numeroDocumentoPersona = numeroDocumentoPersona,
                                                                        tipoDocumentoPersona = tipoDocumentoPersona,
                                                                        codigoCiudad = codigoCiudad,
                                                                        fechaDemandaEmpresa = fechaDemandaEmpresa,
              )


                status=200
                response['result']=True
                response['data']={
                    'id_demanda_empresa_obj':demanda_empresa_obj.id
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


                demanda_empresa_obj=DemandaEmpresaModel.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print(demanda_empresa_obj)

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
                demanda_empresa_obj=DemandaEmpresaModel.objects.filter(id=int(request.query_params.get('id')))

                if len(demanda_empresa_obj)==0:
                    response['detail'] ='demanda_empresa no existe en laborapp'
                elif demanda_empresa_obj[0].is_active is False:
                    response['detail'] ='demanda_empresa ya se encuentra inactiva en laborapp'
                elif len(demanda_empresa_obj)==1 and demanda_empresa_obj[0].is_active is True:
                    demanda_empresa_obj[0].is_active=False
                    demanda_empresa_obj[0].save()
                    status=200

                    response['detail'] ='demanda_empresa fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', demanda_empresa_obj))

            except Exception as error:
                response['detail'] = f'error:{error}'


            return Response({"data":response,},status=status)
