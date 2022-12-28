dados=[]
arq =open('lista.txt','r')

while True:
    print('== MENU ==')
    print('== 1 Cadastrar==')
    print('==2 Listar==')
    print('3 remover')
    opcao=input('Opção?')


    if opcao=='1':

        dados.append(input('Digite o item:'))
        print('item adicionado.')

    elif opcao =='2':
        for item in dados:
            print('--'*20)
            print(item)
            print('--' * 20)

    elif opcao =='3':
        item=input('item a ser removido?')
        if item in dados:
            dados.remove(item)
        print('item removido')

    arq=open("lista.txt",'w')
    for item in dados:
        arq.write(item+'\n')


    arq.close()

