

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




def put_info():

    text:str = f"""\

time.ctime()

Señor.
Juez civil de pequeñas causas -Laboral Bogotá (Repardo)
E.S.D

Referencia : Demanda
Demandante : MARIELA CENEDY PINTO BECERRA
Demandado : Politécnico Rechimbo


Hello,
This is a formal letter
    Thank you very much and we look forward to serving you.

Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them. So when they were old enough, she sent them out into the world to seek their fortunes.
The first little pig was very lazy. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but he was somewhat lazy too and he built his house out of sticks. Then, they sang and danced and played together the rest of the day.
The third little pig worked hard all day and built his house with bricks. It was a sturdy house complete with a fine fireplace and chimney. It looked like it could withstand the strongest winds.

The next day, a wolf happened to pass by the lane where the three little pigs lived; and he saw the straw house, and he smelled the pig inside. He thought the pig would make a mighty fine meal and his mouth began to water.
So he knocked on the door and said:

So he huffed and he puffed and he blew the house down! The wolf opened his jaws very wide and bit down as hard as he could, but the first little pig escaped and ran away to hide with the second little pig.
The wolf continued down the lane and he passed by the second house made of sticks; and he saw the house, and he smelled the pigs inside, and his mouth began to water as he thought about the fine dinner they would make.
So he knocked on the door and said:

Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them. So when they were old enough, she sent them out into the world to seek their fortunes.
The first little pig was very lazy. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but he was somewhat lazy too and he built his house out of sticks. Then, they sang and danced and played together the rest of the day.
The third little pig worked hard all day and built his house with bricks. It was a sturdy house complete with a fine fireplace and chimney. It looked like it could withstand the strongest winds.

The next day, a wolf happened to pass by the lane where the three little pigs lived; and he saw the straw house, and he smelled the pig inside. He thought the pig would make a mighty fine meal and his mouth began to water.
So he knocked on the door and said:

So he huffed and he puffed and he blew the house down! The wolf opened his jaws very wide and bit down as hard as he could, but the first little pig escaped and ran away to hide with the second little pig.
The wolf continued down the lane and he passed by the second house made of sticks; and he saw the house, and he smelled the pigs inside, and his mouth began to water as he thought about the fine dinner they would make.
So he knocked on the door and said:

Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them. So when they were old enough, she sent them out into the world to seek their fortunes.
The first little pig was very lazy. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but he was somewhat lazy too and he built his house out of sticks. Then, they sang and danced and played together the rest of the day.
The third little pig worked hard all day and built his house with bricks. It was a sturdy house complete with a fine fireplace and chimney. It looked like it could withstand the strongest winds.

The next day, a wolf happened to pass by the lane where the three little pigs lived; and he saw the straw house, and he smelled the pig inside. He thought the pig would make a mighty fine meal and his mouth began to water.
So he knocked on the door and said:

So he huffed and he puffed and he blew the house down! The wolf opened his jaws very wide and bit down as hard as he could, but the first little pig escaped and ran away to hide with the second little pig.
The wolf continued down the lane and he passed by the second house made of sticks; and he saw the house, and he smelled the pigs inside, and his mouth began to water as he thought about the fine dinner they would make.
So he knocked on the door and said:

    """
    return text


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

    def generate_pdf(self):
        self.show(put_info())
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
