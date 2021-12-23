#libraries to generate the pdf
import time
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
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
    __doc=None
    __page:list=[]
    __styles=None


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
        self.__styles=getSampleStyleSheet()

        self.__styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    def add_paragraph(self, ptext:str, style='Justify'):

        if style=='Justify':
            self.__page.append(Paragraph(ptext, self.__styles["Justify"]))
        else:
            self.__page.append(Paragraph(ptext, self.__styles["Normal"]))
        self.__page.append(Spacer(1, 12))

    def add_text(self, text:str, space=0):
        for line in text.splitlines():
            self.__page.append(Paragraph(line, self.__styles["Normal"]))
        self.__page.append(Spacer(1, 12))






    def generate_pdf(self):
        self.__doc.build(self.__page)

pdf_generator=PdfGenerator()
pdf_generator.set_features(
                 "demanda_51.pdf",
                 letter,
                 72,
                 72,
                 72,
                 18)
text=f"""\
The third little pig worked hard all day and built his house with bricks. It was a sturdy house complete with a fine fireplace and chimney. It looked like it could withstand the strongest winds.
The next day, a wolf happened to pass by the lane where the three little pigs lived; and he saw the straw house, and he smelled the pig inside. He thought the pig would make a mighty fine meal and his mouth began to water.
So he knocked on the door and said:

"""
pdf_generator.add_paragraph(ptext=text)
pdf_generator.generate_pdf()
