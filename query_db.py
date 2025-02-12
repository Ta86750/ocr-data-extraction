import sqlite3

# Connect to the database
conn = sqlite3.connect("patient_data.db")
cursor = conn.cursor()

# Fetch all records from 'forms_data'
cursor.execute("SELECT * FROM forms_data")
rows = cursor.fetchall()

# Print results
print("\nStored Data in Database:")
for row in rows:
    print(row)

conn.close()
