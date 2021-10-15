from BuilderClass import BuilderClass


class BuilderSerializer(BuilderClass):
#class BuilderSerializer:


    def __init__(self, appName: str, fields: list, nameFile:str):
        BuilderClass.__init__(self, appName, fields, nameFile)

    def add_imports(self):
        imports = f"""\
from rest_framework import serializers
from {self.appName} import models
"""
        self.fileUtil.writeToFile(self.nameFile, imports, True, True)

    def add_name_class(self):

        print(self.fields.__str__())

        class_name = f"""\

class {self.appName.capitalize()}Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.{self.appName.capitalize()}
        fields = {self.fields.__str__()}

        """
        self.fileUtil.writeToFile(self.nameFile, class_name, True, True)


    def add_attri(self, attri:list)->None:
        pass

    def add_method(self, methods:str):
        pass
