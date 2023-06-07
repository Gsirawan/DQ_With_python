import streamlit as st
from home import home_page
from view_data import view_data_page
from data_processing import data_processing_page

st.sidebar.title('👁️ Menu')
page = st.sidebar.selectbox('Select a page', ['Home', 'View Data', 'Data Processing'])

if page == 'Home':
    home_page()
elif page == 'View Data':
    view_data_page()
elif page == 'Data Processing':
    data_processing_page()

if 'df' in st.session_state and st.sidebar.button('Export Data as CSV'):
    from data_utils import df_to_base64
    df = st.session_state.df
    b64 = df_to_base64(df)  # Convert DataFrame to base64
    st.sidebar.markdown(f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV File</a>', unsafe_allow_html=True)
