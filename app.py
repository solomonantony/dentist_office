import streamlit as st
import pandas as pd
from database import get_connection, add_patient
st.title("Dentist Office - Patient Records")
connection = get_connection()
patient_dataframe = pd.read_sql_query("Select * from Patient", connection)
connection.close()
st.subheader("Current Patients")
st.dataframe(patient_dataframe)

st.subheader("New Patient Intake")
with st.form("patient_intake_form"):
    full_name = st.text_input("Full Name")
    address = st.text_input("Address (street, City, State, zip)")
    phone = st.text_input("Phone Number")
    emergency_contact = st.text_input("Emergencu Contact (Name and phone)")
    medical_history = st.text_area("Brief Medical History")
    submitted = st.form_submit_button("Submit and Save Record")
if submitted:
    if full_name and phone:
        new_patient_id = add_patient(full_name, address, phone, emergency_contact, medical_history)
        st.success(f"Patient record created.  Patient ID: {new_patient_id}")
    else:
        st.error("Full name and phone number are required.")
from database import get_connection, add_patient, get_all_providers, get_all_rooms, get_all_patients,add_appointment, get_appointment_for_date
st.subheader("Schedule Appointment")
patients_dataframe = get_all_patients()
providers_dataframe = get_all_providers()
rooms_dataframe = get_all_rooms()
with st.form("schedule_appointment_form"):
    selected_patient_name=st.selectbox("Patient", patients_dataframe["fullName"])
    selected_provider_name=st.selectbox("Provider", providers_dataframe["name"])
    selected_room_type=st.selectbox("Room", rooms_dataframe["roomType"])
    visit_reason=st.selectbox("Visit Type", ["Routine Cleaning", "Filling", "Consultation"]) 
    appointment_date=st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    duration = st.number_input("Duration (minutes)", min_value=15, max_value=180, value=30, step=15)
    schedule_submitted=st.form_submit_button("Confirm Slot")
if schedule_submitted:
    selected_patient_id=int(patients_dataframe.loc[patients_dataframe["fullName"]==selected_patient_name, "patientID"].iloc[0])
    selected_provider_id=int(providers_dataframe.loc[providers_dataframe["name"]==selected_provider_name, "providerID"].iloc[0])
    selected_room_id=int(rooms_dataframe.loc[rooms_dataframe["roomType"]==selected_room_type,"roomID"].iloc[0])

    new_appointment_id=add_appointment(
        selected_patient_id, selected_provider_id,selected_room_id,
        str(appointment_date), str(appointment_time), duration, visit_reason)
    st.success(f"Appoitnment scheduled.  Appointment ID: {new_appointment_id}")
st.subheader("View Appointments for a Date")
view_date=st.date_input("Select a date to view", key="view_date")
appointments_dataframe= get_appointment_for_date(str(view_date))
st.dataframe(appointments_dataframe)

