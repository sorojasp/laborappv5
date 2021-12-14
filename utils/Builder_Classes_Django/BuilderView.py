from BuilderClass import BuilderClass


class BuilderView(BuilderClass):

    __respHTTP = None

    def __init__(self, appName: str, fields: list, nameFile: str):
        BuilderClass.__init__(self, appName, fields, nameFile)

        self.import_models()


    def add_imports(self):
        imports = f"""\
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from {self.appName}.models import {self.appName[0].upper()+self.appName[1:]}Model

import json

#import models from another apps

{self.import_models()}

"""
        self.fileUtil.writeToFile(self.nameFile, imports, True, True)

    def add_name_class(self):
        name_class: str = f"""\

class {self.appName[0].upper()+self.appName[1:]}Views(APIView):

"""
        self.fileUtil.writeToFile(self.nameFile, name_class, True, True)

    def add_attri(self, attr: str):
        attr_class: str = f"""\

        queryset = {self.appName[0].upper()+self.appName[1:]}Model.objects.all()

        """
        self.fileUtil.writeToFile(self.nameFile, attr_class, True, True)

    def add_method(self, method_str):
        methods_class: str = f"""\

        def get(self, request,  format=None, *args, **kwargs):
            try:

                status=200
                amount=str(request.query_params.get('amount'))
                response={self._corchete_abre}
                    'result':None,
                    'data':None,
                    'detail':None
                    {self._corchete_cierra}

                data=None

                if amount =='one':
                    find_{self.appName}= {self.appName[0].upper()+self.appName[1:]}Model.objects.filter(id=int(request.query_params.get('id')))
                    print(find_{self.appName})
                    data=find_{self.appName}
                elif amount =='all':
                    all_{self.appName}={self.appName[0].upper()+self.appName[1:]}Model.objects.all()
                    data=all_{self.appName}

                response['data']=json.loads(serializers.serialize('json', data))
                response['result']=True
                response['detail']= "consulta exitosa"
                status=200
            except Exception as error:
                print("** error in get request  of {self.appName}:  ",error)
                response['result']=False
                response['detail']= str(error)
                status=500

            return Response({self._corchete_abre}"data":response,
                            {self._corchete_cierra},status=status)


        def post(self, request, *args, **kwargs):

            status=500
            response={self._corchete_abre}
                'result':False,
                'data':None,
                'detail':None
                {self._corchete_cierra}

            persona=None
            municipio=None
            try:

                {self.create_object_sentences()}


                status=200
                response['result']=True
                response['data']={self._corchete_abre}
                    'id_{self.appName}_obj':{self.appName}_obj.id
                {self._corchete_cierra}
            except Exception as e:
                response['details']=str(e)

            return Response(response,status=status)


        def patch(self,request,format=None,pk=None):

            status=500

            response={self._corchete_abre}
                'result':False,
                'data':None,
                'detail':None
                {self._corchete_cierra}
            data_to_update={self._corchete_abre}
                 'email':None,
                 'password':None
                 {self._corchete_cierra}

            try:

                print("data: ", request.data)


                {self.appName}_obj={self.appName[0].upper()+self.appName[1:]}Model.objects.update_or_create(id=request.query_params.get('id'),
                                                                            defaults=request.data)

                print({self.appName}_obj)

                status=200
                response['result']=True
                response['detail']='Actualización realizada con éxito'

            except Exception as error:
                print('error in update process:', error)
                response['detail']=f'{self._corchete_abre}str(error){self._corchete_cierra}'


            return Response(response,status=status)




        def delete(self,request,format=None,pk=None):
            status=500

            response={self._corchete_abre}
                'result':False,
                'data':None,
                'detail':None
                {self._corchete_cierra}

            try:
                id=request.query_params.get('id')
                {self.appName}_obj={self.appName}Model.objects.filter(id=int(request.query_params.get('id')))

                if len({self.appName}_obj)==0:
                    response['detail'] ='{self.appName} no existe en laborapp'
                elif {self.appName}_obj[0].is_active is False:
                    response['detail'] ='{self.appName} ya se encuentra inactiva en laborapp'
                elif len({self.appName}_obj)==1 and {self.appName}_obj[0].is_active is True:
                    {self.appName}_obj[0].is_active=False
                    {self.appName}_obj[0].save()
                    status=200

                    response['detail'] ='{self.appName} fue dada de baja con éxito'
                    response['result']=True
                    response['data']=json.loads(serializers.serialize('json', {self.appName}_obj))

            except Exception as error:
                response['detail'] = f'error:{self._corchete_abre}error{self._corchete_cierra}'


            return Response({self._corchete_abre}"data":response,{self._corchete_cierra},status=status)






        """

        self.fileUtil.writeToFile(self.nameFile, methods_class, True, True)



    def create_object_sentences(self)->str:

        native_type_data:list=['int', 'float','str','bool','dict','pk','datetime','email','date','image']
        first_part_create:str=f'                {self.appName}_obj={self.appName[0].upper()+self.appName[1:]}Model.objects.create('+'\n'
        command:str=''
        data_of_anoter_models:str=''

        for field in self.fields_types:
            field_splited:list= field.split(":")
            name_field:str=field_splited[0]
            type_field:str=field_splited[1]


            if type_field in  native_type_data:

                command=f'                      {name_field} = request.data["{name_field}"]'+','+'\n'+'              '+command
            else:

                conditional=f"                if request.data['{name_field}_id']!='None':"+'\n'
                statement=f"                    {name_field} = {type_field[0].upper()+type_field[1:]}Model.objects.get(id=request.data['{name_field}_id'])"+'\n'

                data_of_anoter_models=data_of_anoter_models+conditional+statement


                command=f'                      {name_field} = {name_field}'+','+'\n'+'              '+command

        return data_of_anoter_models+'\n'+first_part_create + command + ')'
