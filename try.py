import os
 
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

for data in lista:
    mancare0.append(data[0])
    gazda0.append(data[1])
    comunale0.append(data[2])
    credite0.append(data[3])
    transport0.append(data[4])
    neprevazute0.append(data[5])

mancare = []
gazda = []
comunale = []
credite = []
transport = []
neprevazute = []

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

print(mancare0)



