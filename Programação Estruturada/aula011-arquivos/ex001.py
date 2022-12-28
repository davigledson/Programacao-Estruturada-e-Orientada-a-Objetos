import csv
arq = open("dados1.csv",'w',newline='')
try:
    gravador = csv.writer(arq)
    gravador.writerow(['Nome','Idade','Sexo'])
    gravador.writerow(['Davi','19','M'])
    gravador.writerow(['Saitama','25','M'])
    gravador.writerow(['Ana','21','F'])
    arq.close()
    print('gravado com suscesso')

except:
    print('erro gravando arquivo')