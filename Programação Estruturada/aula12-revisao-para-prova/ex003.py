import csv
arquivo =open('dados.csv','w',newline='')
gravador=csv.writer(arquivo)
gravador.writerow(['pastel','2 reais'])
gravador.writerow(['cuscuz','4 reais'])
gravador.writerow(['suco','3 reais'])
arquivo.close()
print('Gravado com sucesso')