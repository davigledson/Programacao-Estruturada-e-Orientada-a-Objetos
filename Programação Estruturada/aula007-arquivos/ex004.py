arquivo =open('nomes.txt','w')

for x in range(3):
    nome=input('Digite o nome:')
    arquivo.write(nome + '\n')

arquivo.close()