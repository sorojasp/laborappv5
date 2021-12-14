

#libraries to generate the pdf
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# libraries to store the pdf

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

#another libraries

import random


class PdfGenerator:

    __doc:None
    __page:list=[]
    __styles:None

    def __init__(self):
        pass

    def set_features(self,
                     name_pdf_file:str,
                     pagesize:str,
                     rightMargin:int,
                     leftMargin:int,
                     topMargin:int,
                     bottomMargin:int):
        self.__doc = SimpleDocTemplate(name_pdf_file,pagesize=pagesize,
                                rightMargin=rightMargin,leftMargin=leftMargin,
                                topMargin=topMargin,bottomMargin=bottomMargin)

    def set_styles(self, style_text='Justify'):
        self.__styles=getSampleStyleSheet()
        self.__styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    def add_text(self, text:str, space=0):
        """
        Add text to the pdf line by line
        """

        if type(text)==list:
            for f in text:
                self.add_text(f)
        else:
            ptext = f'<font size="12">{text}</font>'
            self.__page.append(Paragraph(ptext, self.__styles["Normal"]))
            if space==1:
                self.add_space()
            self.add_space()

    def add_space(self, ):
        self.__page.append(Spacer(1, 12))

    def show(self, text:str):
        "Prints all the lines in the text multiline string"
        text = text.splitlines()
        for line in text:
            if ".png" in line:
                self.add_image(line)
            elif "ctime()" in line:
                self.add_text(time.ctime())
            else:
                self.add_text(line)

    def add_image(self, img):
        im = Image(img, 2*inch, 2*inch)
        self.__page.append(im)

    def show(self, text:str):
        "Prints all the lines in the text multiline string"
        text = text.splitlines()
        for line in text:
            if ".png" in line:
                self.add_image(line)
            elif "ctime()" in line:
                self.add_text(time.ctime())
            else:
                self.add_text(line)



    def show(self, text):
        "Prints all the lines in the text multiline string"
        text = text.splitlines()
        for line in text:
            if ".png" in line:
                self.add_image(line)
            elif "ctime()" in line:
                self.add_text(time.ctime())
            else:
                self.add_text(line)

    def generate_pdf(self, content:str):
        self.show(content)
        self.__doc.build(self.__page)


"""
# to make a test
pdf_generator=PdfGenerator()
pdf_generator.set_features(
                 "demanda_48",
                 letter,
                 72,
                 72,
                 72,
                 18)
pdf_generator.set_styles()
pdf_generator.generate_pdf()
"""

# start to save the file
#path = default_storage.save('tmp/demanda.pdf', ContentFile(files[0].read()))
#tmp_file = os.path.join(settings.MEDIA_ROOT, path)
