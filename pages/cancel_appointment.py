import streamlit as st
import pandas as pd
from datetime import date
from database import get_all_patients, get_appointments_for_patient, cancel_appointment_by_id
patients_dataframe = get_all_patients()

st.subheader("Cancel Appointment")
selected_patient_name=st.selectbox("Patient", patients_dataframe["fullName"])
patient_appointments= get_appointments_for_patient(selected_patient_name)
selected = st.dataframe(patient_appointments, on_select = "rerun", selection_mode="single-row")
if selected.selection.rows:
    selected_index=selected.selection.rows[0]
    selected_appointment_row = patient_appointments.iloc[selected_index]
    st.write(f"Selected appointment: {selected_appointment_row['appointmentID']}")
    confirm = st.checkbox("I confirm the deletion")
    if st.button("Delete appointment"):
        if confirm:
            st.write(f"About to delete ID: {selected_appointment_row['appointmentID']}, type: {type(selected_appointment_row['appointmentID'])}")
            rows_deleted=cancel_appointment_by_id(int(selected_appointment_row['appointmentID']))
        else:
            st.warning("Appointment not found")
        st.rerun()
    else:
        st.warning("Please check the confirmation box before deleting")

