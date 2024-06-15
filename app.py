import streamlit as st
import pandas as pd


st.title("Healthcare Management System")
st.write("Welcome to the Healthcare Management System.")


menu = ["Home", "Patient Records", "Appointments", "Analytics"]
choice = st.sidebar.selectbox("Menu", menu)

patients_data = pd.DataFrame(
    {
        "PatientID": [101, 102, 103, 104],
        "Name": ["vinayk", "mayuresh  upare", "yash ranpise", "ganesh magar"],
        "Age": [35, 28, 42, 50],
        "Gender": ["Male", "male", "Male", "male"],
        "Condition": ["Diabetes", "Hypertension", "Asthma", "Obesity"],
    }
)

appointments_data = pd.DataFrame(
    {
        "AppointmentID": [1, 2, 3, 4],
        "PatientID": [101, 102, 103, 104],
        "Date": ["2024-06-15", "2024-06-16", "2024-06-17", "2024-06-18"],
        "Time": ["10:00 AM", "11:30 AM", "2:00 PM", "4:30 PM"],
        "Doctor": ["Dr. krishna", "Dr.shriganesh", "Dr.ram ", "Dr. raj"],
    }
)

if choice == "Home":
    st.write("Welcome to the Home page.")

elif choice == "Patient Records":
    st.subheader("Patient Records")
    st.write(patients_data)

elif choice == "Appointments":
    st.subheader("Appointments")
    st.write(appointments_data)

elif choice == "Analytics":
    st.subheader("Analytics")
    st.write("Here you can visualize analytics.")

    st.bar_chart(patients_data["Age"])
