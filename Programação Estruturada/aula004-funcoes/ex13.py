lista=[]
def cadastrar():
    nome=input("Digite o nome:")
    lista.append(nome)
    print('cadastrado com sucesso')

def listar():
    lista.sort()
    for c in  lista:
        print(c)
    print(f'{len(lista)} Clientes cadastrados')

def excluir():
    nome=input('Nome a ser removido:')
    if nome in lista:
        lista.remove(nome)
        print('Removido com sucesso')
    else:
        print('nome não encontrado')

'''**** MENU ****
1 Cadastrar
2 Listar
3 Excluir
4 Sair
Escolha uma opção: 
'''

while True:
    print('** MENU **')
    print('1 Cadastrar')
    print('2 Listar')
    print('3 Excluir')
    opcao=int(input('Qual opção?'))
    if opcao ==4:

        break
    elif opcao ==1:
        cadastrar()
    elif opcao==2:
        listar()
    elif opcao==3:
        excluir()
    else:
        'Opção invalida'



