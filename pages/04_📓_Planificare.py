import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

#-------------------------------------------------------------------------------------------
#Head
st.write("# We need a Plan!")
image = Image.open("Pictures\pexels-divinetechygirl-1181343.jpg")
st.write(image)
st.write("#### Crearea unui plan este partea importanta pentru obținerea sănătații financiare.")
#-------------------------------------------------------------------------------------------
#Body
lista = []
with open("pages\cifre.txt","r") as f:
    data = f.readlines()
    for elem in data:
        lista.append(float(elem))


st.write("##### 1.Decide pentru tine care este scopul,spre ce mergi.Din punct de vedere financiar unde te vezi peste 5 ani și unde ai vrea să fii.")

st.write("##### 2.Lunar pune deoparte :blue[10%] din venitul tău și păstreazăi pentru zile negre:")
st.write(f"Pentru 2023 lunar salariu mediu era: :blue[{lista[1]}]. Respectiv, pentru zile negre pui in jur la :blue[{round((lista[1]/10),-2)}] Lei in fiecare lună.")

st.write("##### 3.Urmărește regula 80/20!")
st.write(f":blue[80%] din venitul tău brut investește în scopul,calea care ai ales-o. :blue[20%] în scopuri personale.Bugetul tău curat pentru anul precedent este de :blue[{lista[0]}] Lei.")
st.write(f"- :blue[{lista[0] / 10 * 8}] Investește")
st.write(f"- :blue[{lista[0] / 10 * 2}] Scopuri personale(cumpara-ti un tort)")
#----------------------------------------------------------------------------------------------------------------------------------------------        
#Butoanele back/next
col1,col2,col3 = st.columns(3)
back = col1.button("Back")
spactiu = col3.write("")
next = col3.button("Next")

if back:
    switch_page("analiza datelor")
if next:
    switch_page("calculator ce daca")