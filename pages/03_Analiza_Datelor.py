import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import os


#----------------------------------------------------------------------------------------------------------------------------------------------        

st.write("# Analiza Datelor pentru anul 2023")
img = Image.open("Pictures\img.jpg")
st.write(img)
#----------------------------------------------------------------------------------------------------------------------------------------------        
#Citirea documentelor si sortarea elementelor de cheltuieli in forma totala
path = r"C:\Users\ucalr\Desktop\Ion\Gestionare de cheltuieli personale\Luni.2023"

os.chdir(path)
lista = []
def read_text_file(file_path): 
    with open(file_path, 'r') as f: 
        lista.append(f.readlines())

for file in os.listdir():
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        read_text_file(file_path)

mancare0 = []
gazda0 = []
comunale0 = []
credite0 = []
transport0 = []
neprevazute0 = []
salariu0 = []
venitpasiv0 = []

for data in lista:
    mancare0.append(data[0])
    gazda0.append(data[1])
    comunale0.append(data[2])
    credite0.append(data[3])
    transport0.append(data[4])
    neprevazute0.append(data[5])
    salariu0.append(data[7])
    venitpasiv0.append(data[8])

mancare = []
gazda = []
comunale = []
credite = []
transport = []
neprevazute = []
salariu = []
venitpasiv = []

def filtru(x,y):
    for i in x:
        noN = i.replace("\n","")
        splited = noN.split(",")
        y.append(float(splited[0]))

filtru(mancare0,mancare)
filtru(gazda0,gazda)
filtru(comunale0,comunale)
filtru(credite0,credite)
filtru(transport0,transport)
filtru(neprevazute0,neprevazute)
filtru(salariu0,salariu)
filtru(venitpasiv0,venitpasiv)

col4,col5 = st.columns(2)
with col4:
    st.header("Total Cheltuieli")
    st.write(pd.DataFrame({
        "Tip": ["Mâncare","Gazdă","Servicii Comunale","Credit/Împrumuturi","Transport","Neprevăzute"],
        "Suma" : [sum(mancare),sum(gazda),sum(comunale),sum(credite),sum(transport),sum(neprevazute)]    }))
    st.write(f"Total:{sum(mancare)+sum(gazda)+sum(comunale)+sum(credite)+sum(transport)+sum(neprevazute)}")
with col5:
    st.header("Total Buget")
    st.write(pd.DataFrame({
        "Tip": ["Salariu","VenitPasiv"],
        "Suma" : [sum(salariu),sum(venitpasiv)]}))
    st.write(f"Total:{sum(salariu)+sum(venitpasiv)} lei.")
#----------------------------------------------------------------------------------------------------------------------------------------------        
#Grafic
chart_data = pd.DataFrame(
        {
            "Tipul":np.array(["1_🥗","2_🏠","3_❄️","4_💳","5_🚌","6_💸"]),
            "Total":np.array([sum(mancare),sum(gazda),sum(comunale),sum(credite),sum(transport),sum(neprevazute)]),
        })
st.line_chart(chart_data, x = "Tipul", y = "Total", color = "#abd1ff",y_label="Suma",x_label="Mâncare                     Gazdă                     ServiciiC                     Credit/Împr            Transport            Neprevăzute")


#----------------------------------------------------------------------------------------------------------------------------------------------        
#Butoanele back/next
col1,col2,col3 = st.columns(3)
back = col1.button("Back")
spactiu = col3.write("")
next = col3.button("Next")

if back:
    switch_page("expence manager")
if next:
    switch_page("planificare")



