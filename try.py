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
    
print(lista) 
