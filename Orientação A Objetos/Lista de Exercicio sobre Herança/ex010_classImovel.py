class Imovel:
    def __init__(self,tipo,endereco,valor):
        self.tipo = tipo
        self.endereco = endereco
        self.valor = valor

    def setTipo(self,tipo):
        self.tipo=tipo

    def getTipo(self):
        return self.tipo

    def setValor(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco

    def info(self):
        print('Tipo: ',self.tipo)
        print('Endereco ',self.endereco)
        print('Valor:',self.valor)

'''casa1=Imovel('apartamento','rua 19',5000)
casa1.info()'''