import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page



st.title("Manager de Cheltuieli Personale")
image = Image.open('Pictures\FG.jpg')
st.image(image)
st.write("- Această aplicație te va ajuta să fii mai apropae de sănătatea financiară personală")
st.write("## Ce este sănătatea financiară?!")
st.write("- Sănătatea Financiară este libertatea inimii și minții față de orice îngrijorare “Ce dacă” a vieții.")
schimb = st.button("# Let's Go")
if schimb:
   switch_page("pașii de acțiune")





