
#arq=open('dados3.csv','r')
#print(arq.read())


import csv
arq=open('dados3.csv','r')
leitor =csv.reader(arq)

dados =[]
for linha in leitor:
    dados.append(linha)
#print(dados)
#print(dados[1])
#print(dados[3][0])

arq.close()

while True:
    aluno =input('Aluno:')
    serie = input('Serie:')
    curso = input('Curso:')
    dados.append([aluno,serie,curso])
    resp =input('Digita outro? [S/N]')
    if resp == 'n': break

arq=open('dados3.csv','w')
gravador =csv.writer(arq)
gravador.writerows(dados)
arq.close()
print('gravado com sucesso')