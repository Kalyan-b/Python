import streamlit as st
import pandas as pd
import numpy as np

# Streamlit is an open-source Python library for building interactive web applications.
# Internally, it uses React (JavaScript) for rendering the frontend,
# but as a developer, you only need Python code to create apps.

# ------------------------
# Title
# ------------------------
st.title("Hello World")

# Display simple text
st.write("My first Streamlit app 🚀")

# ------------------------
# Creating a simple DataFrame
# ------------------------
df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

# Displaying DataFrame
st.write("Here’s a sample DataFrame:")
st.write(df)

# ------------------------
# Creating line chart
# ------------------------
# np.random.randn(rows, cols) generates random numbers from a normal distribution
chart_data = pd.DataFrame(
    np.random.randn(20, 3),  # 20 rows, 3 columns
    columns=['a', 'b', 'c']
)

st.write("Random data line chart:")
st.line_chart(chart_data)
