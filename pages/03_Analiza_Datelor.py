import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.write("# Analiza Datelor")
st.write("- Aici vei putea vedea un raport anual pentru venitul și cheltuielile tale.")
img = Image.open("Pictures\img.jpg")
st.image(img)
option = st.selectbox(
    "Alege anul",
    ("2022","2023","2024"),index=None)

col1,col2,col3 = st.columns(3)
back = col1.button("Back")
spactiu = col3.write("")
next = col3.button("Next")

if back:
    switch_page("expence manager")
if next:
    switch_page("planificare")

col4,col5 = st.columns(2)
prima = col4.write(pd.DataFrame({
    "Tip": ["Mâncare","Gazdă","Servicii Comunale","Credit/Împrumuturi","Transport","Neprevăzute"],
    "Suma" : [1,2,3,4,5,6]
}))

with open("Luni.2024\Ien.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(float(splited[0]))
with open("Luni.2023\dec.txt","r") as file:
            data = file.readlines()
            listaIen23 = []
            for i in data:
                noN = i.replace("\n","")
                splited = noN.split(",")
                listaIen23.append(float(splited[0]))
    
chart_data = pd.DataFrame(
        {
            "Tipul":np.array(["1_🥗","2_🏠","3_❄️","4_💳","5_🚌","6_💸"]),
            "Ienuarie(2024)":np.array([lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]]),
            "Decembrie(2023)":np.array([listaIen23[0],listaIen23[1],listaIen23[2],listaIen23[3],listaIen23[4],listaIen23[5]])
        })
st.line_chart(chart_data, x = "Tipul", y = ["Decembrie(2023)","Ienuarie(2024)"], color = ["#e54b22", "#abd1ff"],y_label="Suma",x_label="Mâncare                     Gazdă                     ServiciiC                     Credit/Împr            Transport               Neprevăzute")
