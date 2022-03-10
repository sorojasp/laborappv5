from Director import Director
from BuilderClass import BuilderClass
from BuilderBaseClass import BuilderBaseClass
from BuilderSerializer import BuilderSerializer
from BuilderUrls import BuilderUrls
from BuilderView import BuilderView
from BuilderModels import BuilderModels
import os

appName: str = "conflicto_despidoSJC"#Nombre de la app
nameFile_baseClass = f'{appName.capitalize()}.py'#Nombre de la clase base
"""
attributes = [
'id:pk',
"fechaDemandaEmpresa:datetime",
"codigoCiudad:CodigoCiudad",
"tipoDocumentoPersona:str",
"numeroDocumentoPersona:str",
"NItEmpresa:int",
"idContrato:Contrato",
"fechaPropuestaRadicacionDemandaEmpresa:datetime",
"fecharRealRadicacionDemandaEmpresa:datetime",
"fechaPropuestaRadicacionDerechoPetiEmpresa:datetime",
"fecharRealRadicacionDerechoPetiEmpresa:datetime",
"informeDesicionFinalDemandaEmpresa:str",
"respuestaFinalDemandaEmpresa:Boolean",
"montoTotalDemandaPersJuri:float"
"superaMinimaCuantiaPersJuri:Boolean",
"is_active:Boolean"
              ]#atributos de la app
"""
attributes = [
'idDemandaPersonaNatural:DemandaPersonaNatural',
'idDemandaEmpresa:DemandaEmpresa',
'fechaInicioContrato:datetime',
'tipoContrato:str',
'idContrato:Contrato',
'fechaDespido:datetime',
'montoDinero_DSJC:str',
'id:pk',
'is_active:Boolean'
             ]

"""
conflictoDespidoSJC

idConflictoDespidoSJC INT (60) NOT NULL AUTO_INCREMENT,
idDemandaPersonaNatural INT (60)  NULL, /*llave foranea desde demanda persona Natutal*/
idDemandaEmpresa INT (60)  NULL,  /*llave foranea desde demanda a empresa */
fechaInicioContrato DATE NOT NULL, /* llave foranea desde contrato */
tipoContrato VARCHAR(100) NOT NULL,/* agregado sobre diseño incial, 13,mar,2019*/
idContrato INT (60) NOT NULL,
fechaDespido DATE  NULL,
montoDinero_DSJC INT (60) NULL,

"""



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
