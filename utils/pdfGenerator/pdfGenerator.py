

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


doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)



page=[]
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))


def add_image(img):
    im = Image(img, 2*inch, 2*inch)
    page.append(im)


def add_space():
    page.append(Spacer(1, 12))


def add_text(text, space=0):
    if type(text)==list:
        for f in text:
            add_text(f)
    else:
        ptext = f'<font size="12">{text}</font>'
        page.append(Paragraph(ptext, styles["Normal"]))
        if space==1:
            add_space()
        add_space()

def show(text):
    "Prints all the lines in the text multiline string"
    text = text.splitlines()
    for line in text:
        if ".png" in line:
            add_image(line)
        elif "ctime()" in line:
            add_text(time.ctime())
        else:
            add_text(line)


# =============================== The content =======================

text = """
python_logo.png
time.ctime()

Giovanni Gatto
Via Leonardo Da Vinci
tel. 335556566

Hello,
This is a formal letter
    Thank you very much and we look forward to serving you.
"""



# ===========================================================

show(text)
doc.build(page)
os.system("echo form_letter.pdf")



def set_name_file(file_name:str)->bool:
    """Generate a number to add a namefile, if this
       combination exists, then save the file: but if not exist
       then generate a number until the file not exists to save it
     """

    number_file=random.randint(0, 10000)

    print(os.path.exists(f"../../tmp/demanda_{number_file}.pdf"))


    while os.path.exists(f"../../tmp/demanda_{number_file}.pdf"):
        number_file=random.randint(0, 9)
        print("gg", number_file)

    print("path_file", f"../../tmp/demanda_{number_file}.pdf")


set_name_file("")
