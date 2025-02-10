# utils/auth.py
import streamlit as st
from hashlib import sha256

# This is for login work.

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def register_user(username, password):
    if username in st.session_state['user_data']:
        st.error("Username already exists")
    else:
        st.session_state['user_data'][username] = hash_password(password)
        st.success("Registration successful!")

def login_user(username, password):
    hashed_password = hash_password(password)
    if username in st.session_state['user_data'] and st.session_state['user_data'][username] == hashed_password:
        st.session_state['logged_in'] = True
        st.session_state['username'] = username
    else:
        st.error("Invalid username or password")