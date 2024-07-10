import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.write("# Ce daca,lunar,pun deoparte:")

suma = 0
if "suma" in st.session_state:
    suma = st.session_state["suma"]

start = st.number_input("Pui deoparte: ",value=suma)
suma = st.slider("Pui deoparte:", 0,5000,start)

old_suma = 0
if "suma" in st.session_state:
    old_suma = st.session_state["suma"]

st.session_state["suma"] = suma


if old_suma != suma:
    switch_page("calculator ce daca")

un_an = suma * 12
trei_an = suma * 36
cinci_an = suma * 60
st.write(f"### Timp de 1 ani strangi: :red[{un_an}]")
st.write(f"### Timp de 3 ani strangi: :red[{trei_an}]")
st.write(f"### Timp de 5 ani strangi: :red[{cinci_an}]")

#----------------------------------------------------------------------------------------------------------------------------------------------
#Butoanele back/next
col1,col2,col3 = st.columns(3)
back = col1.button("Back")
spactiu = col3.write("")
next = col3.button("Next")

if back:
    switch_page("planificare")
if next:
    switch_page("succes")