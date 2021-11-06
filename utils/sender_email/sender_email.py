
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#files library
import os


class SenderEmail:
    """made with this tutorial:  https://realpython.com/python-send-email/#sending-fancy-emails"""
    """ habilitar el correo https://myaccount.google.com/u/1/lesssecureapps?pli=1"""


    __sender_email:str
    __smtp_server:str
    __port:int  # For starttls
    __password_email:str
    __text_obj=""
    __message:MIMEMultipart=None
    __body:str



    def __init__(self, sender_email="recyappbeta1@gmail.com",
                       smtp_server="smtp.gmail.com",
                       port=465,
                       password_email= "#Stiven19111985",
                       body = "This is an email with attachment sent from Python"):

                       self.__sender_email=sender_email
                       self.__smtp_server=smtp_server
                       self.__port=port
                       self.__password_email=password_email
                       self.__body=body

                       self.create_mesagge_obj()



    def create_mesagge_obj(self)->None:
        """
        """

        self.__message=MIMEMultipart()

    def set_email(self, subject:str)->None:
        """
        """
        self.__message["From"] = self.__sender_email
        self.__message["Subject"] = subject
        self.__message.attach(MIMEText(self.__body, "plain"))



    def attach_file(self, path_file:str):

        try:

            with open(path_file, "rb") as attachment:


                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {path_file}",
                    )

            # Add attachment to message and convert message to string
            self.__message.attach(part)
            self.__text_obj = self.__message.as_string()
            return True
        except FileNotFoundError:
            print("Wrong file or file path")
            return False



    def send_email(self,  receiver_email:str)->bool:

        print(self.__smtp_server, self.__port, self.__sender_email, self.__password_email, )

        self.__message["To"] = receiver_email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=context) as server:

            server.login(self.__sender_email, self.__password_email)
            server.sendmail(self.__sender_email, receiver_email, self.__text_obj)


s_email=SenderEmail()
s_email.set_email("Helloooooo =)")

if s_email.attach_file("../../tmp/demanda.pdf"):
    s_email.send_email("stivenorlandorojaspulido@gmail.com")
