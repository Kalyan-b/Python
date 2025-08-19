import streamlit as st
import pandas as pd

# ------------------------
# Streamlit Basics Example
# ------------------------
st.title("Streamlit Widgets Demo")

# ------------------------
# Text Input
# ------------------------
name = st.text_input("Enter your name:")

if name:
    st.write("👋 Hello,", name)

# ------------------------
# Slider Input
# ------------------------
age = st.slider("Enter your age:", 0, 100, 25)  # Default = 25

# No need for 'if age' since slider always returns a value
st.write("🎂 You are", age, "years old")

# ------------------------
# Selectbox Input
# ------------------------
languages = ["", "Python", "Java", "C/C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language:", languages)

if choice:
    st.write("💻 You selected:", choice)

# ------------------------
# File Uploader
# ------------------------
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Here’s your data:")
    st.dataframe(df)  # st.dataframe() allows scrolling if data is large

# ------------------------
# Info
# ------------------------
st.info("ℹ️ Learn more at: https://streamlit.io")
