import streamlit as st
from PIL import Image

image = Image.open("Pictures\motivational-memes-20.webp")
st.write(image)