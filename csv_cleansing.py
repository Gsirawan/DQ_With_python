import streamlit as st
import pandas as pd
import base64

# Function to convert a DataFrame to a base64 encoded CSV, which will be used to create a download link
def df_to_base64(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return b64

# Create a sidebar menu
st.sidebar.title('👁️ Menu')
page = st.sidebar.selectbox('Select a page', ['Home', 'View Data', 'Data Processing'])

# Home
if page == 'Home':
    st.title('Home Page')
    st.write("Welcome to our application! Use the sidebar to navigate to different pages.")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
        st.session_state.df = df  # Store the DataFrame in st.session_state
        st.success("CSV file uploaded successfully!")


# View Data
elif page == 'View Data':
    st.title('-')
    st.subheader("📊 View Data")

    if 'df' in st.session_state:
        df = st.session_state.df
        st.dataframe(df)
        
        st.subheader('Column Names')
        columns_df = pd.DataFrame(df.columns.tolist(), columns=["Column Names"])  # Create DataFrame with column names
        st.table(columns_df)  # Show column names as a table
    else:
        st.error(
            "Data not available. Please go to the Home page and load a CSV file.")

# Data Processing
elif page == 'Data Processing':
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

# Export button in the sidebar       
if 'df' in st.session_state and st.sidebar.button('Export Data as CSV'):
    df = st.session_state.df
    b64 = df_to_base64(df)  # Convert DataFrame to base64
    st.sidebar.markdown(f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV File</a>', unsafe_allow_html=True)