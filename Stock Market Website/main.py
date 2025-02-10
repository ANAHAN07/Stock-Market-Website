# main.py
import streamlit as st
from utils.auth import register_user, login_user

# Initialize session state
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Sidebar for login/registration
if not st.session_state['logged_in']:
    st.sidebar.title("Login/Register")
    option = st.sidebar.selectbox("Select", ["Login", "Register"])
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')

    if option == "Register":
        if st.sidebar.button("Register"):
            register_user(username, password)
    else:
        if st.sidebar.button("Login"):
            login_user(username, password)
            if st.session_state['logged_in']:
                st.success("Login successful!")

# Navigation after login
if st.session_state['logged_in']:
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Home", "Dashboard", "Compare", "Calculator", "Currency Exchange", "AI Chatbox", "Learn About Treading", "Contact to Website Author"])

    if page == "Home":
        from pages.home import home_page
        home_page()
    elif page == "Dashboard":
        from pages.dashboard import dashboard_page
        dashboard_page()
    elif page == "Compare":
        from pages.compare import compare_page
        compare_page()
    elif page == "Calculator":
        from pages.calculator import calculator_page
        calculator_page()
    elif page == "Currency Exchange":
        from pages.currency_exchanger import currency_exchange_page
        currency_exchange_page()
    elif page == "AI Chatbox":
        from pages.ai_chatbox import ai_chatbox
        ai_chatbox()
    elif page == "Learn About Treading":
        from pages.learn_tread import learn_trading
        learn_trading()
    elif page == "Contact to Website Author":
        from pages.contact_author import contact_box
        contact_box()

st.write("Copyright © 2025 [Ahnaf Mahmud Towseem Ahan](https://www.facebook.com/ahnafNahan). [All rights reserved](https://github.com/ANAHAN07/Project-from-songjog-course/blob/main/Stock%20Market%20Website/LICENSE).")      # LICENSE AND OWENERSHIP