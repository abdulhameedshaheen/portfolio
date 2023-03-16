import streamlit as st
from sendemail import send_email


st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("your email address")
    raw_message = st.text_area("your Message")
    message = f"""\
Subject: New Email from {user_email}
    
From: {user_email}
{raw_message}
"""
    buttom = st.form_submit_button("Submit")

    if buttom:
        send_email(message)
        st.info("Your Email Sent Successfully")
