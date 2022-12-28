arquivo =open("clientes.txt",'r')
clientes = arquivo.readlines()

for nome in clientes:
    print(nome.rstrip('\n')) # ou end=""
arquivo.close()