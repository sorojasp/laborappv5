from abc import ABC, abstractmethod
from FileUtil import FileUtil

class BuilderClass(ABC):
    """Python Interface for logger hierarchy
    Methods:
    _init_ --
    log -- Abstract method; it will be implemented by other classes
    """
    _corchete_abre: str = "{"
    _corchete_cierra: str = "}"
    appName: str = None
    fields_types: list = None
    fields: list = None
    fileUtil: FileUtil = FileUtil()
    nameFile: str = None

    def __init__(self, appName: str, fields: list, nameFile: str):
        self.appName = appName
        self.fields_types=fields
        self.fields = self.set_fields(fields)
        self.fileUtil.writeToFile(nameFile, '', True, True)
        self.nameFile=nameFile
        print(self.nameFile)

    @abstractmethod
    def add_imports(self, imports:str):
        raise Exception("NotImplementedException")

    @abstractmethod
    def add_name_class(self, names_class: str):
        raise Exception("NotImplementedException")

    @abstractmethod
    def add_attri(self, attr: str):
        raise Exception("NotImplementedException")

    @abstractmethod
    def add_method(self, attr: str):
        raise Exception("NotImplementedException")

    def get_params_individual(self, fields: list) -> str:
        """método devuelve los valores individuales de la siguiente forma **upz=data["upz"], direccion=data["direccion"], lat_lon=data["lat_lon"]**
         se hace pensando en las views"""
        params = ''
        for field in fields:
            if field !="id":
                params = params + f'{field}=data["{field}"], '
        return params

    def get_params_individual__str(self, fields: list) -> str:
        """método devuelve los valores individuales de la siguiente forma **upz=upz, direccion=direccion, lat_lon=lat_lon **
                 se hace pensando en las views"""

        params = ''
        for field in fields:
            if field != "id":
                params = params + f'{field}={field}, '
        return params

    def get_params_str(self, fields):
        params = ''
        for field in fields:
            if field!="id":
                params = params + f'{field}, '
        return params

    def set_conditionals_update(self, fields,fileUtil: FileUtil, fileName:str) -> None:
        i = 0
        conditionals = None
        for field in fields:
            print(field)
            print(field != "id")
            if str(field) != "id":
                conditionals = f"""\
                if key == '{fields[i]}':
                    obj.{fields[i]} = data["{fields[i]}"]"""
                fileUtil.writeToFile(fileName, conditionals, True, True)
            i = i + 1

    def set_fields(self, fields:list)->list:
        """configuración de los campos, separa los nombres de los tipos de datos"""
        new_fields = []

        for field in fields:
            new_fields.append(field.split(":")[0])
        return new_fields

    def import_models(self)->str:

        native_type_data:list=['int', 'float','str','bool','dict','pk','datetime','email','date','image']
        import_models:str=''

        for field in self.fields_types:
            field_splited:list= field.split(":")
            name_field:str=field_splited[0]
            type_field:str=field_splited[1]



            if type_field not in  native_type_data:
                import_models=import_models+ f"from {name_field}.models import {name_field.capitalize()}Model"+'\n'

        return import_models
