import warnings
from transformers import pipeline
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

# Suppress warnings and logs
warnings.simplefilter('ignore')


ocr = pipeline('image-to-text', model="microsoft/trocr-base-handwritten")

# Function to perform OCR on the selected image file
def perform_ocr():
    # Open file dialog to select image
    file_path = filedialog.askopenfilename()
    if file_path:
        # Open the image using PIL
        image = Image.open(file_path)
        
        # Perform OCR on the image
        result = ocr(image)
        
        # Display OCR result in GUI
        result_text.config(state=tk.NORMAL)
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "digital text:\n")
        for item in result:
            result_text.insert(tk.END, item['generated_text'] + "\n")
        result_text.config(state=tk.DISABLED)

# Create GUI window
root = tk.Tk()
root.title("Handwritten Text Recognition")

# Button to perform OCR
ocr_button = tk.Button(root, text="Select Image", command=perform_ocr)
ocr_button.pack(pady=10)

# Text widget to display OCR result
result_text = tk.Text(root, height=10, width=50)
result_text.pack(padx=10, pady=10)
result_text.config(state=tk.DISABLED)

# Run the GUI
root.mainloop()
