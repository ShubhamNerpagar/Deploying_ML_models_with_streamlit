import streamlit as st

# Give your app title
st.title("Decoding Automobile")

# Header
st.header("Main Header")

# Sub-header
st.subheader("Sub Header")

# Markdown
st.markdown("Markdown Text")
st.markdown("# Header 1")
st.markdown("## Header 2")

# Caption
st.caption("This is caption")

# Code Block
st.code("""import pandas as pd
pd.read_csv(my_csv_file)
        """)

# Text
st.text("Basic Text")

# Latex
st.latex("x = 2^2")

# Divder
st.text("Text above divider")
st.divider()
st.text("Text below divider")

# St.write
st.write("smoe randome text")