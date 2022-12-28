class Produto:


    def __init__(self,nome,__estoque):
        self.nome=nome
        self.__estoque=__estoque
    def info(self):
        print(f'{self.nome} / {self.__estoque}')

    def incluir(self,qtd):
        self.__estoque +=qtd

    def vender(self,qtd):
        self.__estoque -=qtd

p1=Produto('nescau',0)
p1.nome='nescau'

p1.incluir(5)
p1.info()
p1.incluir(2)
p1.info()
p1.vender(6)
p1.info()