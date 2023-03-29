import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)

with col2:
    st.title("Richard Ostkamp")
    content = """
    Hello, I'm Richard Ostkamp, and this is my Python Showcase. I started programming with a ZX Spectrum,
    learning BASIC and Z80 machine code. I programmed text adventures and wireframe graphics.
    I am now proficient in using functions and OOP, which seems a million miles away from where I started.
    """
    st.info(content)