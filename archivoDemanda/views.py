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
class ArchivoDemandaView(APIView):

    def post(self,  request, *args, **kwargs):

        file_copy=None
        status=200
        response={
            'result':None,
            'data':None,
            'detail':None
            }

        try:

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
            pdf_generator.generate_pdf()



            s_email=SenderEmail()
            s_email.set_email("Helloooooo =)", "Hi", "I hope all is well")

            if s_email.attach_file(f"./{file_name_full}"):
                s_email.send_email("stivenorlandorojaspulido@gmail.com")

            print("file =( : ", open(f"./{file_name_full}", 'rb'))

            

            #os.remove(file_name_full)

            print("** Pdf generate successfully")
            response['result']=True
            response['detail']= "** Pdf generated and sended successfully"





        except Exception as err:
            print("** error to generate and send the pdf:  ",err)
            response['result']=False
            response['detail']= str(err)
            status=500


        #return Response(response, status=status)
        return FileResponse(open(f"./{file_name_full}", 'rb'), content_type='application/pdf')



"""
path = default_storage.save('tmp/demanda.pdf', ContentFile(files[0].read()))
tmp_file = os.path.join(settings.MEDIA_ROOT, path)
"""
