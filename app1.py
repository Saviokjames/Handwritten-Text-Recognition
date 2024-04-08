from flask import Flask, render_template, request
from transformers import pipeline
from PIL import Image
import io

app = Flask(__name__)

# Initialize OCR pipeline
ocr = pipeline('image-to-text', model="SmartPy/handwritten-text-recognition")

# Function to perform OCR on the uploaded image
def perform_ocr(image):
    # Perform OCR on the image
    result = ocr(image)
    return result

@app.route('/')
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

    # Perform OCR on the image
    result = perform_ocr(image)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
