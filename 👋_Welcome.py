import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page



st.title("Manager de Cheltuieli Personale")
st.write("- “Do not save what is left after spending; instead spend what is left after saving.” – Warren Buffett")
st.write("- “A big part of financial freedom is having your heart and mind free from worry abut the what-ifs of life.” - Suze Orman, Personal Finance")
st.write("- Your financial health is essentially an evaluation of your ability to handle your financial needs and wants.")
image = Image.open('Pictures\FG.jpg')
st.image(image)
st.write("###### Înainte ca să începem recomandăm să aveți datele despre venituri și cheltuieli pentru ultimele 3 luni.")
schimb = st.button("# Let's Go")
if schimb:
   switch_page("expence manager")



