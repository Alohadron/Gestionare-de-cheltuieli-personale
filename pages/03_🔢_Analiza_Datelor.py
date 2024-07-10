import streamlit as st
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
path = 'Luni.2023'


lista = []
def read_text_file(file_path): 
    with open(file_path, 'r') as f: 
        lista.append(f.readlines())

for file in os.listdir(path):
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        read_text_file(file_path)

lista_2 = []
for elem in lista:
    lista_3 = []
    for elem_2 in elem:
        lista_3.append(float(elem_2))
    lista_2.append(lista_3)

df = pd.DataFrame(lista_2,columns = ["Mancare","Gazda","Servicii Comunale","Credite/Impr","Transport","Neprevazute","TotalCheltuieli","Salariu","VenitPasiv","TotalBuget"])
#print(df)
total_mancare = sum(df.loc[:,"Mancare"])
total_gazda = sum(df.loc[:,"Gazda"])
total_comunale = sum(df.loc[:,"Servicii Comunale"])
total_credite = sum(df.loc[:,"Credite/Impr"])
total_transport = sum(df.loc[:,"Transport"])
total_neprevazute = sum(df.loc[:,"Neprevazute"])
total_cheltuieli = total_mancare+total_gazda+total_gazda+total_credite+total_transport+total_neprevazute

total_salariu = sum(df.loc[:,"Salariu"])
total_venitpasiv = sum(df.loc[:,"VenitPasiv"])
total_venit = total_salariu+total_venitpasiv

diferenta = int(total_venit - total_cheltuieli)
media_salariu = int(total_venit/12)

col4,col5 = st.columns(2)
with col4:
    st.header("Total Cheltuieli")
    st.write(pd.DataFrame({
        "Tip": ["Mâncare","Gazdă","Servicii Comunale","Credit/Împrumuturi","Transport","Neprevăzute"],
        "Suma" : [total_mancare,total_gazda,total_gazda,total_credite,total_transport,total_neprevazute]    }))
    st.write(f"Total:{total_cheltuieli}")
with col5:
    st.header("Total Buget")
    st.write(pd.DataFrame({
        "Tip": ["Salariu","VenitPasiv"],
        "Suma" : [total_salariu,total_venitpasiv]}))
    st.write(f"Total:{total_venit} lei.")

#----------------------------------------------------------------------------------------------------------------------------------------------        
#Punem diferenta intr-un file aparte pentru o accesa in planificare
with open("pages\cifre.txt","w") as f:
    f.write(str(diferenta) + "\n")
    f.write(str(media_salariu))
#----------------------------------------------------------------------------------------------------------------------------------------------        
#Grafic
chart_data = pd.DataFrame(
        {
            "Tipul":np.array(["1_🥗","2_🏠","3_❄️","4_💳","5_🚌","6_💸"]),
            "Total":np.array([total_mancare,total_gazda,total_gazda,total_credite,total_transport,total_neprevazute]),
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



