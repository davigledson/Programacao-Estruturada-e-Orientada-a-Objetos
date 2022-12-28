import csv
dados = []
arq=open('estoque.csv','r')
leitor=csv.reader(arq)
for linha in leitor:
    dados.append(linha)

opcao = 1
while opcao<4:
    print('=== MENU ===')
    print('1 cadastrar')
    print('2 Listar')
    print('3 Excluir')
    print('4 Sair')
    opcao=int(input('Opção?'))

    if opcao == 1:
        item =input('Nome do item:')
        qtd =input('Quantidade:')
        dados.append([item,qtd])

        arq =open('estoque.csv','w',newline='')
        grav=csv.writer(arq)
        grav.writerows(dados)
        arq.close()
        print('Cadastrado com sucesso')

    if opcao ==2:
        posicao =0
        for linha in dados:
            print(posicao,linha)
            posicao += 1

    if opcao==3:
        posicao=int(input('Apagar qual?'))
        dados.pop(posicao)
        arq =open('estoque.csv','w',newline='')
        grav=csv.writer(arq)
        grav.writerows(dados)
        arq.close()
        print('arquivo excluido com sucesso')
