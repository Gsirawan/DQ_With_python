import streamlit as st

def data_processing_page():
    st.title('Data Processing')
    process = st.sidebar.selectbox(
        'Select a process', ['Data Cleansing', 'Data Standardization', 'Data Parsing'])

    if process == 'Data Cleansing':
        st.subheader('Data Cleansing')
        # Add your data cleansing code here

    elif process == 'Data Standardization':
        st.subheader('Data Standardization')
        # Add your data standardization code here

    elif process == 'Data Parsing':
        st.subheader('Data Parsing')
        # Add your data parsing code here
