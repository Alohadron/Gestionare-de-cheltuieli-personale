import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import os

st.write("# Expence Manager")
st.write("- Ca să cheltui inteligent ai nevoie de un buget")
st.write("- Selectează luna și introduce datele tale de venit și cheltuieli.")
st.write("### Nota:")
st.write("- Bugetul constă din două secțiuni: salariu și venit pasiv. Venit pasiv poate fi orice altă sursă de bani pe lângă salariu.")
st.write("- Cheltuieli constă din șase secțiuni: mâncare,gazdă,servicii comunale,credite/înprumuturi,transport, și cheltuieli neprevăzute ")
st.write("- Vor fi prezente grafice pentru analiza comporatamentului de venit și cheltuieli.Datele deja introduse pot fi schimbate în orice moment")
option = st.selectbox(
    "Selecteaza luna",
    ("Ienuarie", "Februarie", "Martie","Aprilie","Mai","Iunie","Iulie","August","Septembrie","Octombrie","Noiembrie","Decembrie"),index=None)
#----------------------------------------------------------------------------------------------------------------------------------------------
#Functia de calcul a cheltuierilor pentru fiecare luna
def ChemareLuna(luna,PathLunaPrecedenta):#pui ca parametru luni si acolo unde ai nevoie
    print(luna)
    print(PathLunaPrecedenta)
    print(os.curdir)
    with open(f"Luni.2024/{luna}.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(float(splited[0]))
    st.write("# Buget")
    #Introducerea datelor buget
    imagine = Image.open("Pictures\pexels-maitree-rimthong-444156-1602726.jpg")
    st.image(imagine)
    col3,col4 = st.columns(2)
    salariu = col3.number_input("Salariu",value=lista[7])
    venitPasiv = col3.number_input("Venit Pasiv",value=lista[8])
    total1 = salariu + venitPasiv
    with col4:
        st.header(f"Total: {total1}")
    #Graficul Buget
    st.write("## Graficul Bugetului")
    radiobut = st.radio("",["Luna precedenta","Anul precedent"],horizontal=True)
    if radiobut == "Anul precedent":
        with open(f"Luni.2023\{luna}.txt","r") as file:
            data = file.readlines()
            listaIen23 = []
            for i in data:
                noN = i.replace("\n","")
                splited = noN.split(",")
                listaIen23.append(float(splited[0]))
    
        chart_data1 = pd.DataFrame(
        {
            "Tipul":np.array(["🥗","🏠"]),
            f"{luna}(2024)":np.array([lista[7],lista[8]]),
            f"{luna}(2023)":np.array([listaIen23[7],listaIen23[8]]),
        })
        st.bar_chart(chart_data1, x = "Tipul", y = [f"{luna}(2024)",f"{luna}(2023)"], color = ["#abd1ff","#e54b22"],y_label="Suma",x_label="Salariu                                                                                              Venit Pasiv")
    if radiobut == "Luna precedenta":
        with open(f"{PathLunaPrecedenta}","r") as file:
            data = file.readlines()
            listaIen23 = []
            for i in data:
                noN = i.replace("\n","")
                splited = noN.split(",")
                listaIen23.append(float(splited[0]))
        if luna == "Ienuarie": 
            chart_data = pd.DataFrame(
            {
                "Tipul":np.array(["🥗","🏠"]),
                "Ienuarie(2024)":np.array([lista[7],lista[8]]),
                "Decembrie(2023)":np.array([listaIen23[7],listaIen23[8]])
            })
            st.bar_chart(chart_data, x = "Tipul", y = ["Ienuarie(2024)","Decembrie(2023)"], color = ["#abd1ff","#e54b22"],y_label="Suma",x_label="Salariu                                                                                              Venit Pasiv")
        else:
            path = rf"{PathLunaPrecedenta}"
            resultat = os.path.basename(path).replace(".txt","")
            chart_data = pd.DataFrame(
            {
                "Tipul":np.array(["🥗","🏠"]),
                f"{luna}":np.array([lista[7],lista[8]]),
                f"{resultat}":np.array([listaIen23[7],listaIen23[8]])
            })
            st.bar_chart(chart_data, x = "Tipul", y = [f"{resultat}",f"{luna}"], color = [ "#abd1ff","#e54b22"],y_label="Suma",x_label="Salariu                                                                                              Venit Pasiv")
    st.write("## ------------------------------------------------------------")
    #Introducerea datelor cheltuieli
    st.write("# Cheltuieli")
    img = Image.open("Pictures\pexels-karolina-grabowska-4968631.jpg")
    st.image(img)
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Mâncare",value=float(lista[0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3]) )
    transport = col2.number_input("Transport",value=float(lista[4]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    col1.write(f"## Total: {total}")
    submit = st.button("Expediaza Date")
    if submit:
        with open(f"Luni.2024\{luna}.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total) + "\n")
            f.write(str(salariu) + "\n")
            f.write(str(venitPasiv) + "\n")
            f.write(str(total1))
    with open(f"Luni.2024\{luna}.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(float(splited[0]))
    st.write("## ------------------------------------------------------------")
    #Graficul Cheltuieli
    st.write("## Graficul Cheltuierilor")
    radiobut = st.radio("",["Luna trecuta","Anul trecut"],horizontal=True)
    if radiobut == "Anul trecut":
        with open(f"Luni.2023\{luna}.txt","r") as file:
            data = file.readlines()
            listaIen23 = []
            for i in data:
                noN = i.replace("\n","")
                splited = noN.split(",")
                listaIen23.append(float(splited[0]))
        chart_data = pd.DataFrame(
        {
            "Tipul":np.array(["1_🥗","2_🏠","3_❄️","4_💳","5_🚌","6_💸"]),
            f"{luna}(2024)":np.array([lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]]),
            f"{luna}(2023)":np.array([listaIen23[0],listaIen23[1],listaIen23[2],listaIen23[3],listaIen23[4],listaIen23[5]])
        })
        st.line_chart(chart_data, x = "Tipul", y = [f"{luna}(2024)",f"{luna}(2023)"], color = ["#abd1ff","#e54b22"],y_label="Suma",x_label="Mâncare                     Gazdă                     ServiciiC                     Credit/Împr            Transport            Neprevăzute")
    if radiobut == "Luna trecuta":   
        with open(f"{PathLunaPrecedenta}","r") as file:
            data = file.readlines()
            listaIen23 = []
            for i in data:
                noN = i.replace("\n","")
                splited = noN.split(",")
                listaIen23.append(float(splited[0]))
        if luna == "Ienuarie":    
            chart_data = pd.DataFrame(
            {
                "Tipul":np.array(["1_🥗","2_🏠","3_❄️","4_💳","5_🚌","6_💸"]),
                "Ienuarie(2024)":np.array([lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]]),
                "Decembrie(2023)":np.array([listaIen23[0],listaIen23[1],listaIen23[2],listaIen23[3],listaIen23[4],listaIen23[5]])
            })
            st.line_chart(chart_data, x = "Tipul", y = ["Ienuarie(2024)","Decembrie(2023)"], color = ["#abd1ff","#e54b22"],y_label="Suma",x_label="Mâncare                     Gazdă                     ServiciiC                     Credit/Împr            Transport               Neprevăzute")
        else:
            path = rf"{PathLunaPrecedenta}"
            resultat = os.path.basename(path).replace(".txt","")
            chart_data = pd.DataFrame(
            {
                "Tipul":np.array(["1_🥗","2_🏠","3_❄️","4_💳","5_🚌","6_💸"]),
                f"{luna}":np.array([lista[0],lista[1],lista[2],lista[3],lista[4],lista[5]]),
                f"{resultat}":np.array([listaIen23[0],listaIen23[1],listaIen23[2],listaIen23[3],listaIen23[4],listaIen23[5]])
            })
            st.line_chart(chart_data, x = "Tipul", y = [f"{luna}",f"{resultat}"], color = ["#abd1ff","#e54b22"],y_label="Suma",x_label="Mâncare                     Gazdă                     ServiciiC                     Credit/Împr            Transport               Neprevăzute")
    st.write("## ------------------------------------------------------------")


#Chemarea functiilor
if option == "Ienuarie":
    ChemareLuna("Ienuarie","Luni.2023\dec.txt")
if option == "Februarie":
    ChemareLuna("Februarie","Luni.2024\Ienuarie.txt")
if option == "Martie":
    ChemareLuna("Martie","Luni.2024\Februarie.txt")
if option == "Aprilie":
    ChemareLuna("Aprilie","Luni.2024\Martie.txt")

#----------------------------------------------------------------------------------------------------------------------------------------------        
colo1,colo2,colo3 = st.columns(3)
back = colo1.button("Back")
spactiu = colo3.write("")
next = colo3.button("Next")

if back:
    switch_page("welcome")
if next:
    switch_page("analiza datelor")



