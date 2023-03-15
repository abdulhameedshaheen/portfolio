import streamlit as st

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("your email address")
    message = st.text_area("your Message")
    buttom = st.form_submit_button("Submit")

    if buttom:
        print("done")
