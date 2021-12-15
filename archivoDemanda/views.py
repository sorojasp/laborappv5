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



            number_file=random.randint(0, 10000)

            while os.path.exists(f"./{file_name}_{number_file}.{extension_file}"):
                number_file=random.randint(0, 10000)

            file_name_full:str=f"{file_name}_{number_file}.{extension_file}"


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


            s_email=SenderEmail()
            s_email.set_email("Helloooooo =)", "Hi", "I hope all is well")

            if s_email.attach_file(f"./{file_name_full}"):
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
