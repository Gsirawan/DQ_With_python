# Import necessary libraries
import streamlit as st
import pandas as pd
import sqlalchemy as db
import sqlite3

# Create a sidebar menu
st.sidebar.title('Menu')
page = st.sidebar.selectbox('Select a page', ['Connection', 'View Data', 'Data Processing'])


# Database connection
# Database connection
if page == 'Connection':
    st.title('Database Connection')

    db_type = st.selectbox('Select database type', ['SQLite', 'Other'])
    st.session_state.db_type = db_type  # Store the database type in st.session_state

    if db_type == 'SQLite':
        with st.form(key='sqlite_form'):
            db_path = st.text_input('Database Path', key='db_path')
            submit_button = st.form_submit_button(label='Connect')

        if submit_button:
            db_path = st.session_state.db_path
            # Connect to the SQLite database
            try:
                conn = sqlite3.connect(db_path)
                st.session_state.conn = conn  # Store the connection object in st.session_state
                st.session_state.db_type = db_type  # Store the database type in st.session_state
                st.success("Connected successfully to SQLite database!")
            except Exception as e:
                st.error(f"Failed to connect to SQLite database: {e}")

    elif db_type == 'Other':
        with st.form(key='connection_form'):
            ip = st.text_input('IP Address', key='ip')
            port = st.text_input('Port', key='port')
            username = st.text_input('Username', key='username')
            password = st.text_input('Password', key='password', type='password')
            submit_button = st.form_submit_button(label='Connect')

        if submit_button:
            ip = st.session_state.ip
            port = st.session_state.port
            username = st.session_state.username
            password = st.session_state.password
            # Here, you can use the connection parameters to connect to your database
            # For example, if you're using SQLAlchemy, you can create an engine like this:
            # engine = create_engine(f'mysql+pymysql://{username}:{password}@{ip}:{port}/dbname')

    elif db_type == 'CSV':
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df  # Store the DataFrame in st.session_state
            st.success("CSV file uploaded successfully!")


# View Data
elif page == 'View Data':
    st.title('View Data')
      
    if 'df' in st.session_state:
        df = st.session_state.df
        st.dataframe(df)

    elif 'conn' not in st.session_state:
        st.error("Please connect to a database first.")
        
    else:
        conn = st.session_state.conn
        db_type = st.session_state.db_type  # Retrieve the database type from st.session_state

        if db_type == 'SQLite':
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            tables = [table[0] for table in tables]
        else:
            # Assuming you're using SQLAlchemy for other types of databases
            tables = conn.engine.table_names()

        selected_table = st.selectbox('Select a table', tables)
        df = pd.read_sql_query(f"SELECT * FROM {selected_table} LIMIT 100", conn)
        st.dataframe(df)


# Data Processing
elif page == 'Data Processing':
    st.title('Data Processing')
    process = st.sidebar.selectbox('Select a process', ['Data Cleansing', 'Data Standardization', 'Data Parsing'])
    
    if process == 'Data Cleansing':
        st.subheader('Data Cleansing')
        # Add your data cleansing code here

    elif process == 'Data Standardization':
        st.subheader('Data Standardization')
        # Add your data standardization code here

    elif process == 'Data Parsing':
        st.subheader('Data Parsing')
        # Add your data parsing code here
