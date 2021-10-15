from BuilderClass import BuilderClass


class BuilderBaseClass(BuilderClass):


    def __init__(self, appName: str, fields: list, nameFile: str):
        BuilderClass.__init__(self, appName, fields, nameFile)

    def add_imports(self):
        imports = f"""\
from rest_framework import serializers
#from {self.appName} import models
from external_package.encrypDecrpt.Encriptador_Datos import Encriptador_Datos
from {self.appName} import models as {self.appName}_models
from {self.appName} import serializers
from django.forms.models import model_to_dict
from rest_framework import status
"""
        self.fileUtil.writeToFile(self.nameFile, imports, True, True)


    def add_name_class(self):
        name_class: str = f"""\

class {self.appName.capitalize()}:

"""
        self.fileUtil.writeToFile(self.nameFile, name_class, True, True)

    def add_attri(self, attr: str):
        attr_class: str = f"""\
    serializer_class = serializers.{self.appName.capitalize()}Serializer
    queryset = {self.appName}_models.{self.appName.capitalize()}.objects.all()
        """
        self.fileUtil.writeToFile(self.nameFile, attr_class, True, True)

    def add_method(self, method_str):
        methods_class: str = f"""\

    def __init__(self, serializer, queryset):
        self.serializer_class=serializer
        self.queryset=queryset

    def create_(self, {self.get_params_str(self.fields)}):
        try:
            obj = {self.appName}_models.{self.appName.capitalize()}.objects.create({self.get_params_individual__str(self.fields)})
            obj.save()
            print(obj.id)
            return obj.id, status.HTTP_200_OK, "{self.appName} creado con exito"
        except Exception as error:
            return False, status.HTTP_500_INTERNAL_SERVER_ERROR, error.__str__()


    def get_one_(self, id:int):


        try:
            serializer = self.serializer_class({self.appName}_models.{self.appName.capitalize()}.objects.get(id=id))
            print(f'datos serializado: {self._corchete_abre}serializer.data{self._corchete_cierra}')
            data = {self.appName}_models.{self.appName.capitalize()}.objects.get(id=id).__dict__
            del data['_state']
            return serializer.data, status.HTTP_200_OK, " dato encontrado con exito"

        except Exception as error:
            return False, status.HTTP_500_INTERNAL_SERVER_ERROR, error.__str__()


    def get_all_(self):
        try:
            print(self.queryset)
            serializer = self.serializer_class(self.queryset, many=True)
            return serializer.data, status.HTTP_200_OK, " datos encontrados con éxito"

        except Exception as error:
            return False, status.HTTP_500_INTERNAL_SERVER_ERROR, error.__str__()
"""
        self.fileUtil.writeToFile(self.nameFile, methods_class, True, True)
        self.__add_method_update()

    def __add_method_update(self):
        method_class_update: str = f"""\

    def update_(self, pk: int, data: dict):
        try:
            obj = {self.appName}_models.{self.appName.capitalize()}.objects.get(id=pk)
            print(obj)
            for key in data:
"""
        self.fileUtil.writeToFile(self.nameFile, method_class_update, True, True)
        self.set_conditionals_update(self.fields, self.fileUtil, self.nameFile)

        method_class_update_final: str = f"""\
            obj.save()
            return True, status.HTTP_200_OK, "actualización realizada con éxito"

        except Exception as error:
            return False, status.HTTP_500_INTERNAL_SERVER_ERROR, error.__str__()
        """

        self.fileUtil.writeToFile(self.nameFile, method_class_update_final, True, True)
