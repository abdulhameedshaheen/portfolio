import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("portfolio/images/photo.png")

with col2:
    st.title("Abdulhamid Sheen")
    content = """
    this is my portfolio website 
    this is my portfolio website
    this is my portfolio website
    """
    st.info(content)

content2 = """

       this is my portfolio website 
       this is my portfolio website
       this is my portfolio website
"""
st.write(content2)

df = pandas.read_csv("portfolio/data.csv", sep=";")

col3, empty_col1, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("portfolio/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("portfolio/images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
