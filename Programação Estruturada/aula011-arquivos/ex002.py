import csv
arq = open("dados2.csv",'w',newline='')
try:
    gravador = csv.writer(arq)
    gravador.writerow(['Nome','Idade','Sexo'])
    while True:
        nome=input('Digite o nome:')
        idade=input('Idade:')
        sexo=input('Sexo:')
        gravador.writerow([nome,idade,sexo])
        repetir=input('repetir ?: [S/N]')
        if repetir =='n': break
    arq.close()
    print('gravado com sucesso')

except:
    print('erro gravando arquivo')