import streamlit as st
import pandas as pd

# Read the data
st.markdown("Read the data from the file using pandas")
df = pd.read_csv("/workspaces/Deploying_ML_models_with_streamlit/Basics_of_streamlit/sampledata.csv", dtype=int)
st.dataframe(df)
st.divider()
# Read the data using the write function
st.markdown("Read the data using the write function")
st.write(df)

st.divider()
# Read the data as table
st.markdown("Read the data as table")
st.table(df)

st.metric(label="Metric label", value=900, delta=20, delta_color="normal")

# If the decreasing is positive
st.metric(label="Expenses", value=900, delta=-20, delta_color="inverse")