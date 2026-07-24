import streamlit as st
import pandas as pd
from datetime import date
from database import get_connection, add_patient, get_all_providers, get_all_rooms, get_all_patients,add_appointment, get_appointment_for_date


st.subheader("Schedule Appointment")
patients_dataframe = get_all_patients()
providers_dataframe = get_all_providers()
rooms_dataframe = get_all_rooms()
selected_date = st.date_input("Select a date", value=date.today(), key="query_date")
results = get_appointment_for_date(selected_date)
st.write(f"These are the current appointments for {selected_date}")
st.dataframe(results)

with st.form("schedule_appointment_form"):
    selected_patient_name=st.selectbox("Patient", patients_dataframe["fullName"])
    selected_provider_name=st.selectbox("Provider", providers_dataframe["name"])
    selected_room_type=st.selectbox("Room", rooms_dataframe["roomType"])
    visit_reason=st.selectbox("Visit Type", ["Routine Cleaning", "Filling", "Consultation"]) 
    appointment_time = st.time_input("Appointment Time")
    duration = st.number_input("Duration (minutes)", min_value=15, max_value=180, value=30, step=15)
    schedule_submitted=st.form_submit_button("Request Appointment")

if schedule_submitted:
    selected_patient_id=int(patients_dataframe.loc[patients_dataframe["fullName"]==selected_patient_name, "patientID"].iloc[0])
    selected_provider_id=int(providers_dataframe.loc[providers_dataframe["name"]==selected_provider_name, "providerID"].iloc[0])
    selected_room_id=int(rooms_dataframe.loc[rooms_dataframe["roomType"]==selected_room_type,"roomID"].iloc[0])
    new_appointment_id=add_appointment(
        selected_patient_id, selected_provider_id,selected_room_id,
        str(selected_date), str(appointment_time), duration, visit_reason)
    st.success(f"Appoitnment scheduled.  Appointment ID: {new_appointment_id}")

#view_date=st.date_input("Select a date to view", key="view_date")


