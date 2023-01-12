class Produto:
    def __init__(self,produto,preco,estoque):
        self.produto=produto
        self.preco=preco
        self.estoque=estoque

    def info(self):
        print(f'produto: {self.produto}')
        print(f'preco: {self.preco}')
        print(f'estoque: {self.estoque} \n')

    def vender(self):
        if self.estoque >0:
            self.estoque -= 1
        else:
            print('Sem estoque desse produto.')

produto1=Produto('panela',40,15)

produto1.info()
for c in range(16):
    produto1.vender()

produto1.info()