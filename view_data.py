import streamlit as st
import pandas as pd

def view_data_page():
    st.title('View Data')
    st.subheader("📊 View Data")

    if 'df' in st.session_state:
        df = st.session_state.df
        st.dataframe(df)
        
        st.subheader('📓 Header')
        columns_df = pd.DataFrame(df.columns.tolist(), columns=["Column Names"])  # Create DataFrame with column names
        st.table(columns_df)  # Show column names as a table
    else:
        st.error("Data not available. Please go to the Home page and load a CSV file.")
