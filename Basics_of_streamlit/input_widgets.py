import streamlit as st
import pandas as pd

# Buttons
primary_btn = st.button(label="Primary", type="primary")
secondary_btn = st.button(label="secondary", type="secondary")


if primary_btn:
    st.write("Hello from primary")


if secondary_btn:
    st.write("Hello from secondary")

    
# Checkbox
st.divider()

checkbox = st.checkbox("Remember me")

if checkbox:
    st.write("I will remember you")
else:
    st.write("I will forget you")


# Radio Buttons
st.divider()

df = pd.read_csv("Basics_of_streamlit/sampledata.csv")

radio = st.radio("choose a column", options=df.columns[1:], index=0, horizontal=True)
st.write(radio)


# SelectBox
st.divider()
select = st.selectbox("Choose a column", options=df.columns[1:], index=0)

# MutliSelect
st.divider()