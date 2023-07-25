import streamlit as st
from dotenv import load_dotenv
from htmlTemplates import dashboard_html, dashboard_css

def main():
    load_dotenv()
    st.set_page_config(page_title="Dashboad",
                     initial_sidebar_state="collapsed")
    
    st.write(dashboard_css, unsafe_allow_html=True)
    st.write(dashboard_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
