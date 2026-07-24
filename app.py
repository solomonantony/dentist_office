import streamlit as st

def home():
    st.title("Welcome to the Dentist Office")
    st.write("Use the sidebar to navigate")
pg = st.navigation([
    st.Page(home, title="Home", icon="🏠"), #type Windows + . to select an emoji
    st.Page("pages/current_patients.py", title="Current Patients", icon="😯"),
    st.Page("pages/new_patient_intake.py", title="New Patient Intake", icon="📋"),
    st.Page("pages/new_appointment.py", title="New Appointment", icon="📅"),
    st.Page("pages/cancel_appointment.py", title="Cancel Appointment", icon="❌"),
    st.Page("pages/about.py", title="About this app", icon="ℹ️")])

pg.run()



