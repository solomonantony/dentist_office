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
import pandas as pd
def get_all_providers():
    connection = get_connection()
    provider_dataframe = pd.read_sql_query("Select * from provider", connection)
    connection.close()
    return provider_dataframe
def get_all_rooms():
    connection = get_connection()
    rooms_dataframe = pd.read_sql_query("Select * from Room", connection)
    connection.close()
    return rooms_dataframe
def get_all_patients():
    connection = get_connection()
    patients_dataframe = pd.read_sql_query("Select * from patient", connection)
    connection.close()
    return patients_dataframe
def add_appointment(patient_id, provider_id, room_id, appointment_date, appointment_time, duration, visit_reason):
    connection = get_connection()
    cursor=connection.cursor()
    cursor.execute(
        """
        Insert into Appointment(patientID, providerID, roomID, apptDate, ApptTime, duration, visitReason, reminderSentFlag)
        values(?,?,?,?,?,?,?,?)
        """,
        (patient_id, provider_id, room_id, appointment_date, appointment_time, duration, visit_reason,0)
    )
    connection.commit()
    new_appointment_id=cursor.lastrowid
    connection.close()
    return new_appointment_id
def get_appointment_for_date(appointment_date):
    connection = get_connection()
    appointments_dataframe = pd.read_sql_query(
        """
        Select Appointment.appointmentID, Patient.fullName as patientName,
        Provider.name as providerName, Room.roomType,
        Appointment.apptTime, Appointment.duration, Appointment.visitReason
        from Appointment, Patient, Room, Provider 
        where  appointment.patientID=Patient.patientID and
        Appointment.providerID = Provider.providerID and
        Appointment.roomID = Room.roomID and 
        Appointment.apptDate = ?
        order by Appointment.apptTime
        """,
        connection,
        params=(appointment_date,)
    )
    connection.close()
    return appointments_dataframe

if __name__ == "__main__":
    initialize_database()
