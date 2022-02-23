
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
                       smtp_server="smtp.gmail.com",#"smtp.gmail.com"
                       port=587,
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
        Create a object that is needed to set the message
        """

        self.__message=MIMEMultipart()

    def set_email(self,
                   subject:str,
                   header:str,
                   message:str)->None:
                    """
                    Method to set a subject, header and message of a email
                    """
                    html = f"""\
                    <html>
                     <body>
                     <p>{header}</p>
                    <p>{message}<p>
                    <p>Visita nuestro sito web: <a href="http://www.ingnovatech.com/recyapp">RecyApp</a> </p>
                    Salvando nuestro mundo...
                    </p>
                    </body>
                    </html>
                    """
                    #part1 = MIMEText(text, "plain")
                    part2 = MIMEText(html, "html")

                    self.__message["From"] = self.__sender_email
                    self.__message["Subject"] = subject
                    self.__message.attach(part2)
                    #print(self.__message)

    def attach_file(self, path_file:str):

        """

        method to attach a file to a message; path_file contains the path of
        the file what to want attach to the email

        """

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
            print("Wrong file or file path: ")
            return False



    def send_email(self,  receiver_email:str)->bool:
        
        """

        try:
            self.__text_obj = self.__message.as_string()

            #print(self.__smtp_server, self.__port, self.__sender_email, self.__password_email, )

            self.__message["To"] = receiver_email
            context = ssl.create_default_context()
            with smtplib.SMTP(self.__smtp_server, self.__port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(self.__sender_email, self.__password_email)
                server.sendmail(self.__sender_email, receiver_email, self.__text_obj)
                return True
        except Exception as error :
            print("Error meanwhile send the email: "+ str(error))
            return False
        """
        
        msg = """From: Sender
To: Recipient
Subject: This is the message subject

This is the message body.
"""
        
        try:
            s = smtplib.SMTP('199.79.62.144:2083')
            s.login('stivenrojas@ingnovatech.com', '#Stiven1911')
            s.sendmail('stivenrojas@ingnovatech.com', receiver_email, msg)
            s.quit()
        except smtplib.SMTPException:
            print("Error:", sys.exc_info()[0])
            


s_email=SenderEmail()
s_email.set_email("Helloooooo =)", "Hi", "I hope all is well")

if s_email.attach_file("../../tmp/demanda.pdf"):
    s_email.send_email("stivenorlandorojaspulido@gmail.com")
