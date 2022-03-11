from BuilderClass import BuilderClass



class BuilderModels(BuilderClass):

    def __init__(self, appName: str, fields: list, nameFile:str):
        BuilderClass.__init__(self, appName, fields, nameFile)
        print(self.fields_types)

    def add_imports(self):
        imports = f"""\
from django.db import models


#import models from another apps

{self.import_models()}
"""
        self.fileUtil.writeToFile(self.nameFile, imports, True, True)

    def add_name_class(self):
        name_class: str = f"""\
class {self.appName.capitalize()}(models.Model):
"""
        self.fileUtil.writeToFile(self.nameFile, name_class, True, True)

    def add_attri(self, attr: str):
        typePy_typeFieldsDj: dict = self.__map_typePy_typeFieldsDj()
        all_types_field = typePy_typeFieldsDj.keys()
        type_found = False



        for field in self.fields_types:
            type_input: str = str(field).split(":")[1]
            type_found = False
            for type in all_types_field:

                if type_input == str(type):
                    type_found = True
                    attr = f"""\
    {str(field).split(":")[0]} = {typePy_typeFieldsDj[type]}"""
                    self.fileUtil.writeToFile(self.nameFile, attr, True, True)
                    print(f'{str(field).split(":")[0]} = {typePy_typeFieldsDj[type]}')
                    break
            if not type_found:
                attr = f"""\
    {str(field).split(":")[0]} = models.ForeignKey({str(str(field).split(":")[0]).capitalize()}, on_delete=models.CASCADE)"""
                self.fileUtil.writeToFile(self.nameFile, attr, True, True)

                print(f'{str(field).split(":")[0]} = models.ForeignKey({str(str(field).split(":")[0]).capitalize()}, on_delete=models.CASCADE)')


    def __map_typePy_typeFieldsDj(self)->dict:
        """se configura un mapeo entre los tipos de datos de python y los tipos de datos en los campos de Django"""

        typePy_typeFieldsDj: list = {'str': 'models.CharField(max_length=255, null=True, blank=True)',
                                     'email': 'models.EmailField(max_length=255, null=True, blank=True)',
                                     'int': 'models.IntegerField',
                                     'pk': 'models.AutoField(primary_key=True)',
                                     'Boolean':'models.BooleanField(default=True, null=True, blank=True)',
                                     'time': 'models.TimeField(null=True, blank=True)',
                                     'datetime':'models.DateTimeField(null=True, blank=True)',
                                     'file': 'models.FileField()',
                                     'float':'models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)',
                                     'image': 'models.ImageField(upload_to="avatars",blank=True,null=True,verbose_name="Photo")'
                                    }

        return typePy_typeFieldsDj

    def add_method(self, attr: str):
        pass
