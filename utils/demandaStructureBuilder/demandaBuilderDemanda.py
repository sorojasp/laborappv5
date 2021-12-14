

#import pdf generator
#from pdfGenerator import PdfGenerator


## libraries to make a pdf
from reportlab.lib.pagesizes import letter


file_name:str="demanda"
extension_file:str="pdf"

import random
import os


class DemanadaBuilderDemanda:

    nombre_demandante:str
    apellido_demandante:str
    tipo_documento_demandante:str
    lugar_expedicion_documento_demandante:str
    documento_demandante:str
    nombre_empresa:str
    tipo_documento_empresa:str
    documento_empresa:str
    ciudad_empresa:str
    lugar_resisdencia_demandante:str
    header:str
    summary:str
    allText:str


    def __init__(self,nombre_demandante:str,
                 apellido_demandante:str,
                 tipo_documento_demandante:str,
                 lugar_expedicion_documento_demandante:str,
                 documento_demandante:str,
                 nombre_empresa:str,
                 tipo_documento_empresa:str,
                 documento_empresa:str,
                 ciudad_empresa:str,
                 lugar_resisdencia_demandante):

        self.nombre_demandante= nombre_demandante
        self.apellido_demandante= apellido_demandante
        self.tipo_documento_demandante= tipo_documento_demandante
        self.lugar_expedicion_documento_demandante= lugar_expedicion_documento_demandante
        self.documento_demandante= documento_demandante
        self.nombre_empresa= nombre_empresa
        self.tipo_documento_empresa= tipo_documento_empresa
        self.documento_empresa=documento_empresa
        self.ciudad_empresa= ciudad_empresa
        self.lugar_resisdencia_demandante=lugar_resisdencia_demandante

        self.build_header()
        self.build_summary()


    def build_header(self):
        self.header = f"""\



        Señor.
        Juez civil de pequeñas causas -Laboral Bogotá (Repardo)
        E.S.D

        Referencia : Demanda
        Demandante : {self.nombre_demandante}
        Demandado : {self.nombre_empresa}

"""


    def build_summary(self)->str:
            self.summary = f"""\
        Yo {self.nombre_demandante} mayor de edad y domiciliado en Bogotá con {self.tipo_documento_demandante} número {self.documento_demandante} expedia en {self.lugar_expedicion_documento_demandante}, obrando en mi nombre. Presento ante su honorable despacho
        demanda contra {self.nombre_empresa} identifcada con {self.tipo_documento_empresa} {self.documento_empresa}, representada
        legalmente por SOLICITAR REPRESENTANTE LEGAL o quien haga sus veces, entidad con domicilio
        en {self.lugar_resisdencia_demandante}, para que mediante el trámite propio del proceso ordinario laboral de mínima
        cuantía y mediante sentencia se proferan las respectivas condenas que más adelante entraré
        a solicitar, para lo cual me fundamento en los hechos y normas que a continuación relaciono.

""".replace("\n", "")

    def setAllDocument(self)->str:
        self.allText=self.header+self.summary
        return self.allText





demandaBuilder=DemanadaBuilderDemanda("Stiven Orlando",
             "Rojas Pulido",
             "CC",
             "Bogotá D.C",
             "80.865.137",
             "Uniempresarial",
             "NIT",
             "897897",
             "Bogotá D.C",
             "Bogotá D.C")

number_file=random.randint(0, 10000)

while os.path.exists(f"./{file_name}_{number_file}.{extension_file}"):
    number_file=random.randint(0, 10000)

file_name_full:str=f"{file_name}_{number_file}.{extension_file}"
"""
pdf_generator=PdfGenerator()
pdf_generator.set_features(
                 file_name_full,
                 letter,
                 72,
                 72,
                 72,
                 18)
pdf_generator.set_styles()
pdf_generator.generate_pdf(demandaBuilder.setAllDocument())
"""
