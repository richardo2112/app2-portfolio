import streamlit as st
import pandas as pd

data = pd.read_csv("data.csv", sep=";")

st.set_page_config(layout="wide")

left, col1, gutter, col2, right = st.columns([0.2, 1.5, 0.5, 1.5, 0.2])

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

intro_content = """
    Below you can find some of the apps I have built (following Ardit) in Python. Feel free to contact me!
"""
st.write(intro_content)

left, col3, gutter, col4, right = st.columns([0.2, 1.5, 0.5, 1.5, 0.2])

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.image(f"images/{row['image']}")
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.image(f"images/{row['image']}")
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

st.write("[richardostkampwebsite](http://richardostkamp.com)")

