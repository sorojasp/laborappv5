
import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("form_letter.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
import os


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
