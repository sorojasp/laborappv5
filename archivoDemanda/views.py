from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response

#libraries to save files
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings



#import pdf generator
from utils.pdfGenerator.pdfGenerator import PdfGenerator

#import sender email
from utils.sender_email.sender_email import SenderEmail

from django.http import FileResponse
## libraries to make a pdf

from reportlab.lib.pagesizes import letter

file_name:str="demanda"
extension_file:str="pdf"

derecho_peticion_name="derechoPeticion"
derecho_peticion_extension="pdf"

import random
import time
import copy

# libraries to handle of files
import sys
import io
import psutil
import base64

# import class that set law file
from utils.demandaStructureBuilder.demandaBuilderDemanda import DemanadaBuilderDemanda
from utils.demandaStructureBuilder.derechoPeticionBuilder import DerechoPeticionBuilder

class ArchivoDemandaView(APIView):

    def post(self,  request, *args, **kwargs):

        email=None
        file_copy=None
        status=200
        response={
            'result':None,
            'data':None,
            'detail':None
            }
        try:
            email=request.query_params.get("email")
            print("email: ",email)

            demandaBuilder=DemanadaBuilderDemanda(
                                                  request.data['summaryDemanda']["nombreDemandante"],
                                                  request.data['summaryDemanda']["apellidoDemandante"],
                                                  request.data['summaryDemanda']["tipoDocumentoDemandante"],
                                                  request.data['summaryDemanda']["lugarExpedicionDocumentoDemandante"],
                                                  request.data['summaryDemanda']["documentoDemandante"],
                                                  request.data['summaryDemanda']["nombreEmpresa"],
                                                  request.data['summaryDemanda']["tipoDocumentoEmpresa"],
                                                  request.data['summaryDemanda']["documentoEmpresa"],
                                                  request.data['summaryDemanda']["ciudadEmpresa"],
                                                  request.data['summaryDemanda']["lugarResisdenciaDemandante"],
                                                  )

            #Set name of demanda file
            number_file=random.randint(0, 10000)
            while os.path.exists(f"./{file_name}_{number_file}.{extension_file}"):
                number_file=random.randint(0, 10000)
            file_name_full:str=f"{file_name}_{number_file}.{extension_file}"

            #Set name of derecho peticion
            number_file_derechoP=random.randint(0, 10000)
            while os.path.exists(f"./{derecho_peticion_name}_{number_file_derechoP}.{derecho_peticion_extension}"):
                number_file_derechoP=random.randint(0, 10000)
            derecho_name_full:str=f"{derecho_peticion_name}_{number_file_derechoP}.{derecho_peticion_extension}"


            #Generate pdf of "demanda" file
            pdf_generator=PdfGenerator()
            pdf_generator.set_features(
                             file_name_full,
                             letter,
                             72,
                             72,
                             72,
                             30)

            pdf_generator.add_text(f'{time.ctime()}')
            pdf_generator.add_text(demandaBuilder.build_header())
            pdf_generator.add_paragraph(ptext=demandaBuilder.build_summary())

            pdf_generator.add_text("<b>Tipo de proceso: </b>")
            pdf_generator.add_paragraph(ptext=request.data['tipoProceso'])

            #Hechos

            pdf_generator.add_text("<b>Hechos: </b>")

            index:int=1
            for hecho in request.data['hechos']:
                pdf_generator.add_paragraph(ptext=f"{index}"+". "+hecho)
                index+=1

            #Peticiones
            pdf_generator.add_text(f'<b>Peticiones: </b>')
            pdf_generator.add_paragraph(ptext="Solicito al señor juez, que una vez probados los hechos arriba enunciados se declare:")

            index=1
            for peticion in request.data['peticiones']:
                pdf_generator.add_paragraph(ptext=f"  {index}"+". "+peticion)
                index+=1

            #Pruebas
            pdf_generator.add_text("<b>Pruebas: </b>")
            pdf_generator.add_paragraph(ptext="Solicito señor Juez, que se sirva decretar y practicar las siguientes pruebas para que sean tenidas en cuenta al elaborarse el fallo respectivo: ")

            #Pruebas documentales
            index=1
            if len(request.data['pruebas']['documentales'])!=0:
                pdf_generator.add_text("<b>Documentales: </b>")
                for prueba_documental in request.data['pruebas']['documentales']:
                    pdf_generator.add_paragraph(ptext=f"{index}"+". "+prueba_documental)
                    index+=1

            #Pruebas testimoniales
            index=1
            if len(request.data['pruebas']['testimoniales'])!=0:
                pdf_generator.add_text("<b>Testimoniales: </b>")
                for prueba_testimonial in request.data['pruebas']['testimoniales']:
                    pdf_generator.add_paragraph(ptext=f"{index}"+". "+prueba_testimonial)
                    index+=1

            #Competencia
            pdf_generator.add_text("<b>Competencia: </b>")
            pdf_generator.add_paragraph(ptext="Es usted competente ya que yo legitimado por activa preste mis servicios en esta ciudad en la cual está domiciliado al igual que la legitimada por pasiva, además, lo es por la naturaleza del negocio y la razón de la cuantía.")

            #cuantia
            pdf_generator.add_text("<b>Cuantia: </b>")
            pdf_generator.add_paragraph(ptext=request.data['cuantia'])

            #notificaciones
            pdf_generator.add_text("<b>Notificaciones: </b>")
            pdf_generator.add_paragraph(ptext="Para que se efecúen debidamente facilito las siguientes direcciones.")

            #notificaciones demandado
            if len(request.data['notificaciones']['demandado'])!=0:
                pdf_generator.add_text("<b>Demandado: </b>")
                for notficacion_demandado in request.data['notificaciones']['demandado']:
                    pdf_generator.add_paragraph(ptext=notficacion_demandado)

            #notificaciones demandante
            if len(request.data['notificaciones']['demandante'])!=0:
                pdf_generator.add_text("<b>Demandante: </b>")
                for notficacion_demandado in request.data['notificaciones']['demandante']:
                    pdf_generator.add_paragraph(ptext=notficacion_demandado)

            #anexos
            pdf_generator.add_text("Anexos de la demanda: ")
            pdf_generator.add_paragraph(ptext="Los documentos aducidos como pruebas que se encontraban en mi poder.")

            #
            pdf_generator.add_text("Del señor Juez")

            #signature
            signature=""

            for item in request.data['signature']:
                signature=signature+item+'\n'
            pdf_generator.add_text(signature)


            pdf_generator.generate_pdf()

            del pdf_generator


            #*********************** Derecho de petición file******************************************#
            pdf_generator_derechoP=PdfGenerator()
            pdf_generator_derechoP.set_features(
                             derecho_name_full,
                             letter,
                             72,
                             72,
                             72,
                             30)

            derechoBuilder=DerechoPeticionBuilder( request.data['summaryDemanda']["nombreDemandante"],
             request.data['summaryDemanda']["apellidoDemandante"],
             request.data['summaryDemanda']["tipoDocumentoDemandante"],
             request.data['summaryDemanda']["lugarExpedicionDocumentoDemandante"],
             request.data['summaryDemanda']["documentoDemandante"],
             request.data['summaryDemanda']["nombreEmpresa"],
             request.data['summaryDemanda']["tipoDocumentoEmpresa"],
             request.data['summaryDemanda']["documentoEmpresa"],
             request.data['summaryDemanda']["ciudadEmpresa"],
             request.data['summaryDemanda']["lugarResisdenciaDemandante"],)

            pdf_generator_derechoP.add_text(derechoBuilder.build_header())

            pdf_generator_derechoP.add_paragraph(ptext="Asunto: Derecho de Petición. Artículo 23 de la Constitución Política y Ley 1755 de 2015 (Colocar un resumen muy breve de lo que solicita).")

            pdf_generator_derechoP.add_text("Respetados señores: ")

            pdf_generator_derechoP.add_paragraph(ptext= f"yo, {request.data['summaryDemanda']['nombreDemandante']} {request.data['summaryDemanda']['apellidoDemandante']} identificado como aparece al pie de mi firma, de conformidad con lo establecido en el artículo 23 de la Constitución Política, en concordancia con la Ley 1755 de 2015, comedidamente me permito presentar la petición que más adelante se describe.")

            pdf_generator_derechoP.add_text("<b>Hechos: </b>")

            index:int=1
            for hecho in request.data['hechos']:
                pdf_generator_derechoP.add_paragraph(ptext=f"{index}"+". "+hecho)
                index+=1

            pdf_generator_derechoP.add_text("<b>Petición: </b>")
            pdf_generator_derechoP.add_paragraph(ptext=request.data['cuantia'])

            pdf_generator_derechoP.add_text("<b>Finalidad: </b>")
            pdf_generator_derechoP.add_paragraph(ptext=f"Se solicita que la empresa {request.data['summaryDemanda']['nombreEmpresa']} atienda a las peticiones declaradas en el presente derecho petición.")

            pdf_generator_derechoP.add_text("<b>Notificación: </b>")
            pdf_generator_derechoP.add_paragraph(ptext=f"Por favor enviar la correspondencia a través de alguno de los siguientes medios:")

            pdf_generator_derechoP.add_paragraph(ptext=f" - Correo electrónico: {email}")
            pdf_generator_derechoP.add_paragraph(ptext=f" - Dirección de residencia: {request.data['signature'][2].split('Dirección: ')[1]}")
            pdf_generator_derechoP.add_paragraph(ptext=f" - Ciudad: {request.data['summaryDemanda']['lugarResisdenciaDemandante']}")

            pdf_generator_derechoP.add_text("<b>Cordialmente: </b>")

            pdf_generator_derechoP.add_text(signature)






            pdf_generator_derechoP.generate_pdf()

            del pdf_generator_derechoP

            print("** Genera la demanda =) ***")

            #*********************** Derecho de petición file******************************************#




            s_email=SenderEmail()
            s_email.set_email("Demanda generada", "Hola", f"""\

      Hola soy Juan Carlos Pulido,

      En adjunto encontrarás tres archivos; el primero es la demanda que has generado a través de Laborapp, el segundo es el
      derecho de petición que, en caso de no haberlo hecho, debes entregar a tu empleador y el tercer archivo es un instructivo
      del paso a paso que debes seguir para radicar tu demanda ante la rama judicial.



                                  """)



            if s_email.attach_file(f"./{file_name_full}"):
                if s_email.attach_file(f"./{derecho_name_full}"):
                    if s_email.attach_file("./instructivo.pdf"):
                        s_email.send_email(email)

            print("file =( : ", open(f"./{file_name_full}", 'rb'))

            print("** Pdf generate successfully")
            response['result']=True
            response['detail']= "** Pdf generated and sended successfully"


            with open(f"./{file_name_full}", "rb") as f:
                encodedZip = base64.b64encode(f.read())
                f.close()
                response['file_base64']=encodedZip.decode()
                #fileResponse=FileResponse(encodedZip.decode(), content_type='application/pdf')
                os.remove(f"./{file_name_full}")
                #return Response(response, status=status)

            # delete file of derecho
            with open(f"./{derecho_name_full}", "rb") as fl:
                encodedZipl = base64.b64encode(fl.read())
                fl.close()
                response['file_base64_derecho']=encodedZipl.decode()
                #fileResponse=FileResponse(encodedZip.decode(), content_type='application/pdf')
                os.remove(f"./{derecho_name_full}")
                return Response(response, status=status)


        except Exception as err:
            print("** error to generate and send the pdf:  ",err)
            response['result']=False
            response['detail']= str(err)
            status=500

        return Response(response, status=status)




"""
path = default_storage.save('tmp/demanda.pdf', ContentFile(files[0].read()))
tmp_file = os.path.join(settings.MEDIA_ROOT, path)
"""
