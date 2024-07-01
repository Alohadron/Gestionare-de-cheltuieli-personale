import streamlit as st
from PIL import Image

st.title("Manager de Cheltuieli Personale")
st.write("“Do not save what is left after spending; instead spend what is left after saving.” – Warren Buffett")
image = Image.open('fh.jpg')
st.image(image)
st.write("#### Înainte ca să începem recomandăm să aveți datele despre venituri și cheltuieli pentru ultimele 3 luni")
col1, col2, col3 = st.columns(3)
emp1 = col1.write("")
emp2 = col2.link_button("Let's Go","")
emp3 = col3.write("")