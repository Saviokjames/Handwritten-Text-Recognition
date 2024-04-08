from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline
from PIL import Image

import io

app = Flask(__name__)

# Initialize OCR pipelines
ocr1 = pipeline('image-to-text', model="microsoft/trocr-large-handwritten")
ocr2 = pipeline('image-to-text', model="microsoft/trocr-base-handwritten")
ocr3 = pipeline('image-to-text', model="mocrosoft/trocr-small-handwritten")

# Dictionary to store results of each model
results = {'model1': None, 'model2': None}

# Function to perform OCR on the uploaded image based on the selected model
def perform_ocr(image, ocr_model):
    # Perform OCR using the selected model
    result = ocr_model(image)
    return result
def perform_ocr2(image, ocr_model):
    # Perform OCR using the selected model
    result = ocr_model(image)
    return result
def perform_ocr3(image, ocr_model):
    # Perform OCR using the selected model
    result = ocr_model(image)
    return result

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html', error='No selected file')

        # Read the uploaded image file
        image = Image.open(io.BytesIO(file.read()))

        # Determine which OCR model to use based on the button clicked
        if 'ocr1' in request.form:
            ocr_model = ocr1
            results['model1'] = perform_ocr(image, ocr_model)
            return model1_display_results()
        elif 'ocr2' in request.form:
            ocr_model = ocr2
            results['model2'] = perform_ocr2(image, ocr_model)
            return model2_display_results()
        elif 'ocr3' in request.form:
            ocr_model = ocr3
            results['model3'] = perform_ocr3(image, ocr_model)
            return model3_display_results()
             

    return render_template('index.html')

@app.route('/model1_result')
def model1_display_results():
    return render_template('model1_result.html', results=results)


@app.route('/model2_result')
def model2_display_results():
    return render_template('model2_result.html', results=results)

@app.route('/model3_result')
def model3_display_results():
    return render_template('model3_result.html', results=results)


@app.route('/compare')
def compare_results():
    return render_template('compare.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
