# OCR Data Extraction and Database Integration Project

This project automates the extraction of data from patient assessment forms using OCR. The extracted text is converted into structured JSON format and stored in a SQL database.

## Features
- **OCR Extraction:** Uses Tesseract OCR to extract text from scanned forms.
- **Preprocessing:** Applies grayscale conversion and thresholding to improve OCR accuracy.
- **JSON Conversion:** Converts the extracted text into a structured JSON format.
- **Database Integration:** Stores the JSON data in a SQLite database.
- **Documentation:** Complete instructions and code available in this repository.

## Setup Instructions
1. **Install Dependencies:**
   ```bash
   pip install pytesseract opencv-python pdf2image pillow sqlalchemy
