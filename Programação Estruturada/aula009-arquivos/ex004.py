lista=[]
for c in range(5):
    nome=input('Digite o nome:')
    lista.append(nome+'\n')
lista.sort()
##########
arquivo = open('clientes.txt','w')
arquivo.writelines(lista)
arquivo.close()
print(' Arquivo gravado com sucesso')

