import sqlite3

# Connect to SQLite database (creates a new file if it doesn’t exist)
conn = sqlite3.connect("patient_data.db")
cursor = conn.cursor()

# Create table for patient details
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dob TEXT
)
""")

# Create table for storing JSON-formatted assessment data
cursor.execute("""
CREATE TABLE IF NOT EXISTS forms_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    form_json TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(patient_id) REFERENCES patients(id)
)
""")

# Commit changes and close the connection
conn.commit()
conn.close()

print("✅ Database setup complete!")
