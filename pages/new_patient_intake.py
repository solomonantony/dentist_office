# pages/new_patient_intake.py
import streamlit as st
import pandas as pd
from database import get_connection, add_patient
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
