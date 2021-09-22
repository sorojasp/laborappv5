import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EnviadorCorreos:
    """made with this tutorial:  https://realpython.com/python-send-email/#sending-fancy-emails"""
    """ habilitar el correo https://myaccount.google.com/u/1/lesssecureapps?pli=1"""


    __senderEmail:str="recyappbeta1@gmail.com"
    __smtp_server:str = "smtp.gmail.com"
    __port:int = 587  # For starttls
    __password:str = "#Stiven1911"
    __serverObject:smtplib.SMTP=None
    __message:MIMEMultipart=None

    def __init__(self):
        self.__getServerObject()
        self.__setSecurityConnection()
        self.__logginGmail()

    def __getServerObject(self)->bool:
        """se ejemplifica el servidor"""
        try:
            self.__serverObject=smtplib.SMTP(self.__smtp_server, self.__port)
            print("server Object created  ** Ok **")
            return True
        except Exception as e:
            print(e)
            return False

    def __setSecurityConnection(self)->bool:
        """Create a secure SSL context"""
        try:
            context = ssl.create_default_context()
            self.__serverObject.starttls(context=context)
            print("SecurityConnection ** Ok **")
            return True

        except Exception as e:
            print(e)
            return False

    def __logginGmail(self)->bool:
        """login in gmail with the sender email"""

        try:
            self.__serverObject.login(self.__senderEmail, self.__password)
            print("**loggin ok**")
            return True
        except Exception as e:
            print(e)
            return False

    def sendEmail(self, emailReceiver:str, asunto:str, encabezado:str,message:str)->bool:

        try:
            self.__serverObject.sendmail(self.__senderEmail, emailReceiver, self.__setMessage(emailReceiver,message, encabezado, asunto))
            print("message sended")
            return True
        except Exception as e:
            print(e)
            return False

        finally:
            self.__serverObject.quit()


    def __setMessage(self, emailReceiver:str, message:str,encabezado:str, asunto:str)->str:
        self.__message = MIMEMultipart("alternative")
        self.__message["Subject"]=asunto
        self.__message["From"]= "RecyApp"
        self.__message["To"]= emailReceiver

        # Create the plain-text and HTML version of your message

        
        
        html = f"""\
        <html>
         <body>
         <p>{encabezado}</p>
        <p>{message}<p>
        <p>Visita nuestro sito web: <a href="http://www.ingnovatech.com/recyapp">RecyApp</a> </p>
        Salvando nuestro mundo...
        </p>
        </body>
        </html>
        """
        #part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        #self.__message.attach(part1)
        self.__message.attach(part2)
        return self.__message.as_string()
















