from ex010_classImovel import  Imovel

class ImovelNovo(Imovel):
    def __init__(self, tipo, endereco, valor, construtora):
        super().__init__(tipo, endereco, valor)
        self.construtora = construtora

    def setConstrutora(self, construtora):
        self.construtora = construtora

    def getConstrutora(self):
        return self.construtora
    def info(self):
        super().info()
        print('Construtora:',self.construtora)

casanova=ImovelNovo('casa','centro, rua nova',15000,'Contruiçoes Massas')
casanova.info()
