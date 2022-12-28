#arquivo 2
import csv
arquivo=open('dados.csv','r')
leitor =csv.reader(arquivo)
lista=[]
for linha in leitor:
    lista.append(linha)
arquivo.close()

print(lista)
print(lista[0])
print(lista[0][1])