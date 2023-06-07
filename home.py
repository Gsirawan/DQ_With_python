import streamlit as st
import pandas as pd

def home_page():
    st.title('Home Page')
    st.write("Welcome to our application! Use the sidebar to navigate to different pages.")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
        st.session_state.df = df  # Store the DataFrame in st.session_state
        st.success("CSV file uploaded successfully!")
