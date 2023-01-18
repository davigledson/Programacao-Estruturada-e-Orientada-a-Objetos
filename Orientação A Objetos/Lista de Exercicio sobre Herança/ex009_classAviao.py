from ex006_classTransporte import Transporte

class Aviao(Transporte):
    posicao ='chão'
    def __init__(self, fabricante, ano, modelo, posicao, qtdPassageiros):
        super().__init__(fabricante, ano, modelo)
        self.qtdPassageiros=qtdPassageiros
        self.posicao=posicao

    def setPosicao(self, posicao):
        self.posicao = posicao

    def getPosicao(self):
        return self.posicao

    def setQtdPassageiros(self, qtdPassageiros):
        self.qtdPassageiros = qtdPassageiros

    def getQtdPassageiros(self):
        return self.qtdPassageiros

    def decolar(self):
        if self.posicao == 'chão':
            self.posicao = 'Ar'


    def pousar(self):
        if self.posicao == 'Ar':
            self.posicao ='Chão'


    def info(self):
        super().info()
        print('Quantidade de Passageiros',self.qtdPassageiros)
        print('Posição: ',self.posicao)




aviao1=Aviao('GOL',2015,'novo','chão',200)
aviao1.decolar()

aviao1.info()
print('--'*20)
aviao1.pousar()
aviao1.info()


