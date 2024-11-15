import pytesseract
from PIL import Image
import pdfplumber

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

def extract_text_from_pdf(pdf_file):
    resume_text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            resume_text += page.extract_text()
    return resume_text
