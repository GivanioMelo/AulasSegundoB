import os

names = ['Jessa', 'Eric', 'Bob', "Waldyr", "Wesley", "Pereira"]
notas = [10,10,10,10,10,10]

filename = "meuArquivo.txt"
file = open(filename, 'w')

file.write("O arquivo começa aqui\n")
file.write("Nome : Nota\n")

for i in range(len(names)):
    linhaDoArquivo = f"{names[i]} : {notas[i]}\n"
    file.write(linhaDoArquivo)

file.write("O arquivo termina aqui\n")

file.close()

os.system(f"notepad {filename}")

