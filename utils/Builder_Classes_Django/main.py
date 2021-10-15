from Director import Director
from BuilderClass import BuilderClass
from BuilderBaseClass import BuilderBaseClass
from BuilderSerializer import BuilderSerializer
from BuilderUrls import BuilderUrls
from BuilderView import BuilderView
from BuilderModels import BuilderModels
import os

appName: str = "demandaPersonaNatural"#Nombre de la app
nameFile_baseClass = f'{appName.capitalize()}.py'#Nombre de la clase base
attributes = ['ubicacion:Municipios',
              'personaNatural:PersonaNatural',
              'contrato:ContratoLaboral',
              ' fechapropuestaradicaciondemandapersonan:datetime',
              ' fecharrealradicaciondemandapersonan:datetime',
              'fechapropuestaradicacionderechopetipersona:datetime',
              ' fecharrealradicacionderechopetipersonan:datetime',
              'informedesicionfinaldemandapersonan:str',
              'respuestafinaldemandaersonan:str',
              'montototaldemandapersnat:float',
              'superaminimacuantiapersna:str',
              ]#atributos de la app

# Creación del directorio en donde se guardarán los resultados

directory = "results"
this_directory = os.path.dirname(__file__)
absolute_directory = os.path.join(this_directory, directory)
print(absolute_directory)
os.mkdir(absolute_directory)


#Ejemplificación de las clases constructoras de las archivos
builderView: BuilderClass = BuilderView(appName, attributes, f"{directory}/views.py")
#builderBaseClass: BuilderClass = BuilderBaseClass(appName, attributes, f"{directory}/{nameFile_baseClass}")
#builderSerializer: BuilderClass = BuilderSerializer(appName, attributes, f"{directory}/serializers.py")
#builderUrls: BuilderClass = BuilderUrls(appName, attributes, f"{directory}/urls.py")
builderModels: BuilderClass = BuilderModels(appName, attributes, f"{directory}/models.py")

#builders = [builderView, builderBaseClass, builderSerializer, builderUrls, builderModels]

builders=[builderView,builderModels]


for builder in builders:
    director: Director = Director(builder)
    director.builder()
