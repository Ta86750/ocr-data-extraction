import pytesseract
import cv2
import json
import re
from PIL import Image
import sqlite3

# Set Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the image (ensure sample.jpg is on your Desktop)
image_path = "sample.jpg"
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to improve contrast
gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Save the preprocessed image for debugging
cv2.imwrite("preprocessed_sample.jpg", gray)

# Convert to PIL format and perform OCR with page segmentation mode 6
processed_image = Image.fromarray(gray)
text = pytesseract.image_to_string(processed_image, config='--psm 6')

print("Extracted Text:")
print(text)

# Function to convert text to JSON
def parse_text_to_json(raw_text):
    data = {}
    name_match = re.search(r"Patient Name[:\-]*\s*(.+)", raw_text, re.IGNORECASE)
    dob_match = re.search(r"DOB[:\-]*\s*(.+)", raw_text, re.IGNORECASE)
    diagnosis_match = re.search(r"Diagnosis[:\-]*\s*(.+)", raw_text, re.IGNORECASE)
    
    data["patient_name"] = name_match.group(1).strip() if name_match else "Unknown"
    # Clean DOB (replace common OCR errors)
    dob_raw = dob_match.group(1).strip() if dob_match else "Unknown"
    dob_clean = dob_raw.replace("@", "0").replace("|", "1")
    data["dob"] = dob_clean if re.match(r"\d{2}/\d{2}/\d{4}", dob_clean) else "Unknown"
    data["diagnosis"] = diagnosis_match.group(1).strip() if diagnosis_match else "Unknown"
    
    return json.dumps(data, indent=4)

# Convert text to JSON
json_data = parse_text_to_json(text)
print("\nStructured JSON Output:")
print(json_data)

# Function to store JSON data in the SQLite database
def store_data(json_data):
    """Insert extracted JSON data into the database"""
    conn = sqlite3.connect("patient_data.db")
    cursor = conn.cursor()
    
    # Convert JSON string to Python dictionary
    data = json.loads(json_data)
    
    # Debugging Print: Show the data that is going to be inserted
    print("\nInserting Data:")
    print(data)
    
    # Insert into 'patients' table
    cursor.execute("INSERT INTO patients (name, dob) VALUES (?, ?)", (data["patient_name"], data["dob"]))
    patient_id = cursor.lastrowid
    print(f"Inserted Patient ID: {patient_id}")
    
    # Insert full JSON data into 'forms_data' table
    cursor.execute("INSERT INTO forms_data (patient_id, form_json) VALUES (?, ?)", (patient_id, json_data))
    
    conn.commit()
    conn.close()
    
    print(f"✅ Data stored successfully for {data['patient_name']}!")

# Store the data in the database
store_data(json_data)

