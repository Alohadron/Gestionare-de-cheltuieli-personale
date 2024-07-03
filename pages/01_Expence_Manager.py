import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pandas as pd
st.write("# Hai să vedem cât de tare îți place să cheltui")
image = Image.open("Pictures\pexels-karolina-grabowska-4968631.jpg")
st.image(image)
st.write("### Introdu datele despre cheltuielile tale(în lei) pentru ultimele luni.")

option = st.selectbox(
    "Selecteaza luna",
    ("Ienuarie", "Februarie", "Martie","Aprilie","Mai","Iunie","Iulie","August","Septembrie","Octombrie","Noiembrie","Decembrie"),index=None)
#----------------------------------------------------------------------------------------------------------------------------------------------
#Functia de calcul a cheltuierilor pentru fiecare luna
def Ien():
    with open("Luni.2024\Ien.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Ienuarie")
    #Introducerea datelor
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\Ien.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\Ien.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    #Afisharea datelor
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{round(float(lista[0][0]),2)} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
    #Graficul
    st.write("## Graficul Cheltuierilor")
    radiobut = st.radio("## Compara cu: ",["Luna trecuta","Anul trecut"],horizontal=True)
    if radiobut == "Anul trecut":
        with open("Luni.2023\Ien.txt","r") as file:
            data = file.readlines()
            listaIen23 = []
            for i in data:
                noN = i.replace("\n","")
                splited = noN.split(",")
                listaIen23.append(splited)
    
        chart_data = pd.DataFrame(
        {
            "Tipul":np.array(["1_🥗","2_🏠","3_❄️","4_💳","5_🚌","6_💸"]),
            "Ienuarie(2024)":np.array([lista[0][0],lista[1][0],lista[2][0],lista[3][0],lista[4][0],lista[5][0]]),
            "Ienuarie(2023)":np.array([listaIen23[0][0],listaIen23[1][0],listaIen23[2][0],listaIen23[3][0],listaIen23[4][0],listaIen23[5][0],])
        })
        st.line_chart(chart_data, x = "Tipul", y = ["Ienuarie(2024)","Ienuarie(2023)"], color = ["#DC7633", "#229954"],y_label="Suma")
    if radiobut == "Luna trecuta":
        with open("Luni.2023\dec.txt","r") as file:
            data = file.readlines()
            listaIen23 = []
            for i in data:
                noN = i.replace("\n","")
                splited = noN.split(",")
                listaIen23.append(splited)
    
        chart_data = pd.DataFrame(
        {
            "Tipul":np.array(["1_🥗","2_🏠","3_❄️","4_💳","5_🚌","6_💸"]),
            "Ienuarie(2024)":np.array([lista[0][0],lista[1][0],lista[2][0],lista[3][0],lista[4][0],lista[5][0]]),
            "Decembrie(2023)":np.array([listaIen23[0][0],listaIen23[1][0],listaIen23[2][0],listaIen23[3][0],listaIen23[4][0],listaIen23[5][0],])
        })
        st.line_chart(chart_data, x = "Tipul", y = "Ienuarie(2024)", color = "#229954",y_label="Suma")
def Feb():
    with open("Luni.2024\Feb.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Februarie")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\Feb.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\Feb.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***:credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Mar():
    with open("Luni.2024\mar.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Martie")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\mar.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\mar.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Apr():
    with open("Luni.2024\Apr.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Aprilie")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\Apr.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\Apr.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Mai():
    with open("Luni.2024\mai.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Mai")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\mai.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\mai.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Iun():
    with open("Luni.2024\iun.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Iunie")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\iun.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\iun.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Iul():
    with open("Luni.2024\iul.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Iulie")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\iul.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\iul.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Aug():
    with open("Luni.2024\Aug.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## August")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\Aug.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\Aug.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Sept():
    with open("Luni.2024\sep.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Septembrie")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\sep.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\sep.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Oct():
    with open("Luni.2024\oct.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Octombrie")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\oct.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\oct.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Nov():
    with open("Luni.2024\zai.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Noiembrie")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\zai.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\zai.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
def Dec():
    with open("Luni.2024\dec.txt","r") as f:
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## Decembrie")
    col1,col2 = st.columns(2)
    mancare =col1.number_input("Alimentație",value=float(lista[0][0]))
    gazda = col1.number_input("Gazdă",value=float(lista[1][0]) )
    comunale = col1.number_input("Serviciile Comunale",value=float(lista[2][0]) )
    datorii = col2.number_input("Credite/Înprumuturi",value=float(lista[3][0]) )
    transport = col2.number_input("Transport",value=float(lista[4][0]) )
    unexpected = col2.number_input("Cheltuieli Neprevăzute",value=float(lista[5][0]))
    total = mancare + gazda + comunale + datorii + transport + unexpected
    submit = st.button("Expediaza Date")
    if submit:
        with open("Luni.2024\dec.txt","w") as f:
            f.write(str(mancare) + "\n")
            f.write(str(gazda) + "\n")
            f.write(str(comunale) + "\n")
            f.write(str(datorii) + "\n")
            f.write(str(transport) + "\n")
            f.write(str(unexpected) + "\n")
            f.write(str(total))
    with open("Luni.2024\dec.txt","r") as f:#citim a doua oara doc ca sa nu apasam de doua ori butonul
        data = f.readlines()
        lista = []
        for i in data:
            noN = i.replace("\n","")
            splited = noN.split(",")
            lista.append(splited)
    st.write("## ------------------------------------------------------------")
    col3,col4 = st.columns(2)
    col3.metric(label="***Alimentație:***:green_salad:" ,value=f"{lista[0][0]} Lei")
    col3.metric(label="***Gazdă:***:house:" ,value=f"{lista[1][0]} Lei")
    col3.metric(label="***Serviciile Comunale:***:snowflake:" ,value=f"{lista[2][0]} Lei")
    col4.metric(label="***Credite/Înprumuturi:***::credit_card:" ,value=f"{lista[3][0]} Lei")
    col4.metric(label="***Transport:***:bus:" ,value=f"{lista[4][0]} Lei")
    col4.metric(label="***Cheltuieli Neprevăzute:***:money_with_wings:" ,value=f"{lista[5][0]} Lei")
    st.write(f"## Total: {lista[6][0]}")
    st.write("## ------------------------------------------------------------")
#Chemarea functiilor
if option == "Ienuarie":
    Ien()
if option == "Februarie":
    Feb()
if option == "Martie":
    Mar()
if option == "Aprilie":
    Apr()
if option == "Mai":
    Mai()
if option == "Iunie":
    Iun()
if option == "Iulie":
    Iul()
if option == "August":
    Aug()
if option == "Septembrie":
    Sept()
if option == "Octombrie":
    Oct()
if option == "Noiembrie":
    Nov()
if option == "Decembrie":
    Dec()
#----------------------------------------------------------------------------------------------------------------------------------------------        







