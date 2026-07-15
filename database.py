import sqlite3
DB_FILE = "dentist_office.db"

def get_connection():
    connection = sqlite3.connect(DB_FILE)
    connection.execute("PRAGMA foreign_keys=ON")
    return connection
def initialize_database():
    connection = get_connection()
    with open("schema.sql", "r") as schema_file:
        schema_script = schema_file.read()
    connection.executescript(schema_script)
    connection.commit()
    connection.close()
    print("Database initialized")

def add_patient(full_name, address, phone, emergency_contact, medical_history):
    """Inserts a new patient with a complete record and returns the new patientID"""
    connection = get_connection()
    cursor=connection.cursor()
    cursor.execute(
        """
        INSERT INTO Patient(fullName, address, phone, emergencyContact, medicalHistory, recordStatus)
        VALUES(?, ?, ?, ?, ?, ?)
        """,
        (full_name, address, phone, emergency_contact, medical_history,"Complete")
    )
    connection.commit()
    new_patient_id= cursor.lastrowid
    connection.close()
    return new_patient_id

if __name__ == "__main__":
    initialize_database()
