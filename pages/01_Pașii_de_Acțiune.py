import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.write("# Cuprins")
st.write("### 1.Expence Manager - Aici vei putea introduce datele despre venitul și cheltuielile tale pentru orice luna aparte care dorești")
st.write("### 2.Analiza Datelor - În analiza datelor vei putea urmari care a fost progresul tău anual din punct de vedere financiare și analiza situația în fiecare domeniu.")
st.write("### 3.Planificare - În final vom face un plan pentru obținerea sănătății financiare!")

col1,col2,col3 = st.columns(3)
back = col1.button("Back")
spactiu = col3.write("")
next = col3.button("Next")

if back:
    switch_page("welcome")
if next:
    switch_page("expence manager")
