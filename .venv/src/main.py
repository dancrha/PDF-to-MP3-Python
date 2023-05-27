'''
PDF to MP3 Converter
Daniel Crha
05/26/2023*/
'''

import PyPDF2
from gtts import gTTS
from PIL import Image
import pytesseract
import os
from pdf2image import convert_from_path

# Open the PDF file
with open('.venv/src/book3.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)

    # Convert each page of the PDF to an image
    images = convert_from_path('.venv/src/book3.pdf', dpi=300)

    # Extract text from each image using OCR
    text = ""
    for image in images:
        # Convert the image to grayscale for better OCR results
        image = image.convert('L')
        # Perform OCR using pytesseract
        page_text = pytesseract.image_to_string(image)
        text += page_text

    # Create an audio file from the extracted text
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
    else:
        print("No text found in the PDF.")

# Play the saved MP3 file using the default media player
if os.name == 'nt':  # for Windows
    os.system("start output.mp3")
else:  # for macOS and Linux
    os.system("afplay output.mp3")
