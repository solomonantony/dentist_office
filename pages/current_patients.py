# pages/current_patients.py
import streamlit as st
import pandas as pd
from database import get_connection, add_patient
st.title("Dentist Office - Patient Records")
connection = get_connection()
patient_dataframe = pd.read_sql_query("Select * from Patient", connection)
connection.close()
st.subheader("Current Patients")
st.dataframe(patient_dataframe)
