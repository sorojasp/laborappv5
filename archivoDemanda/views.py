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

#libraries to send email
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class ArchivoDemandaView(APIView):

    def post(self,  request, *args, **kwargs):


        files = request.FILES.getlist('demanda')
        print("files: ", files)
        files[0]


        path = default_storage.save('tmp/demanda.pdf', ContentFile(files[0].read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)



        # send emails with attach


        subject = "An email with attachment from Python"
        body = "This is an email with attachment sent from Python"
        sender_email = "recyappbeta1@gmail.com"
        receiver_email = request.query_params.get('email')
        password = "#Stiven19111985"

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        #message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))


        filename = "tmp/demanda.pdf"  # In same directory as script
        #in production the path is = "tmp/demanda.pdf"
        # in develop the path is = tmp\demanda.pdf

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)






        return Response({
                        "hi":"hello"
        }, status=200)
