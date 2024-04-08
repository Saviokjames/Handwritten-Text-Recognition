from flask import Flask, render_template, request
from transformers import pipeline
from PIL import Image
import io

from requests.exceptions import SSLError

# Import requests library
import requests

# Disable SSL verification globally
requests.packages.urllib3.disable_warnings()


app = Flask(__name__)

# Initialize OCR pipelines
ocr1 = pipeline('image-to-text', model="microsoft/trocr-large-handwritten")
ocr2 = pipeline('image-to-text', model="microsoft/trocr-base-handwritten")

# Function to perform OCR on the uploaded image based on the selected model
def perform_ocr(image, ocr_model):
    # Perform OCR using the selected model
    result = ocr_model(image)
    return result

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    # Read the uploaded image file
    image = Image.open(io.BytesIO(file.read()))

    # Determine which OCR model to use based on the button clicked
    ocr_model = None
    if 'ocr1' in request.form:
        ocr_model = ocr1
    elif 'ocr2' in request.form:
        ocr_model = ocr2

    # Perform OCR on the image using the selected model
    if ocr_model:
        result = perform_ocr(image, ocr_model)
    else:
        result = []

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
