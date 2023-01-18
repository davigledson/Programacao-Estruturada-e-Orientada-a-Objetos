from ex004_classTransporte import Transporte

class Carro(Transporte):

    def __init__(self,fabricante,ano,modelo,qtdPortas):
        super().__init__(fabricante,ano,modelo)
        self.qtdPortas = qtdPortas

    def abrirPortaMalas(self):
        print('Portas molas aberto')
    def info(self):
        super().info()
        print('Quantidade de portas:',self.qtdPortas)


carro1=Carro('Ferrari',2000,'Velho',2)
carro1.info()
carro1.abrirPortaMalas()
