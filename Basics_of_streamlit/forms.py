import streamlit as st
import pandas as pd

df = pd.read_csv("Basics_of_streamlit/sampledata.csv")
with st.form("My form"):
     st.write("What would you like to order?")
     appetizer = st.selectbox("Appetizer", options=df.columns[1:])
     Main_Course = st.selectbox("Main Course", options=df.columns[1:])
     Dessert = st.selectbox("Dessert", options=df.columns[1:])
     wine = st.checkbox("Are you bringing you own wine?")
     date = st.date_input("when are you coming?",value=None)
     time = st.time_input("At what time are you coming?",value=None)
     allergy = st.text_input("Any allergies?")

     submitted = st.form_submit_button("Submit")
     if submitted:
          st.write("Appetizer:", appetizer)
          st.write("Main Course:", Main_Course)
          st.write("Dessert:", Dessert)
          st.write("Are you bringing you own wine? ", "yes" if wine else "no")
          st.write("Date of visit : ",date)
          st.write("Time of visit : ", time)
          st.write("Allergy : ", allergy)
     