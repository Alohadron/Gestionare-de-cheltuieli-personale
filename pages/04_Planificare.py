import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import os
from PIL import Image


st.write("# We need a Plan!")
st.write("#### Crearea unui plan este  partea importanta pentru obtinerea sanatatii financiare.")
st.write("1.Decide pentru tine care este scopul,spre ce mergi.Din punct de vedere financiar unde te vezi pester 5 ani si unde ai vrea sa fii.")
st.write("2.Lunar pune deoparte :blue[10%] din venitul tau si pastreazai pentru zile negre.")
# image = Image.open("Pictures\pexels-divinetechygirl-1181343.jpg")
# st.write(image)
#-------------------------------------------------------------------------------------------
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
btotal = sum(salariu)+sum(venitpasiv)
ctotal = sum(mancare)+sum(gazda)+sum(comunale)+sum(credite)+sum(transport)+sum(neprevazute)
diferenta = btotal - ctotal
st.write(f"3.Poti sa observi diferenta de cheltuieli totale si venituri totale pentru anul trecut: :blue[+{diferenta}]Lei. Respectiv respecta regula :blue[80/20]. Pentru scopul tau investeste 80% din venitul tau brut, 20% ii lasi tie pentru nevoi personale.")

#-------------------------------------------------------------------------------------------
#Ce daca?
start = st.number_input("Pui deoparte: ")
with open("pages\Value.txt","w") as f:
    f.write(start)
suma = st.slider("Pui deoparte:", 0,5000)
un_an = suma * 12
trei_an = suma * 36
cinci_an = suma * 60
st.write(f"### Timp de 1 ani strangi: :red[{un_an}]")
st.write(f"### Timp de 3 ani strangi: :red[{trei_an}]")
st.write(f"### Timp de 5 ani strangi: :red[{cinci_an}]")
#-------------------------------------------------------------------------------------------
back = st.button("Back")
if back:
    switch_page("analiza datelor")
