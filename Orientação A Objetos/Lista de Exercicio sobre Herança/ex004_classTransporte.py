class Transporte:
    fabricante=''
    ano=0
    modelo=''
    def __init__(self,fabricante,ano,modelo):
        self.fabricante=fabricante
        self.ano=ano
        self.modelo=modelo

    def setFabricante(self,fabricante):
        self.fabricante=fabricante

    def getFabricante(self):
        return self.fabricante

    def setAno(self, ano):
        self.ano = ano

    def getAno(self):
        return self.ano

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def info(self):
        print('Fabricante:',self.fabricante)
        print('Modelo:', self.modelo)
        print('Ano:', self.ano)

'''carro1=Transporte()
carro1.setFabricante('UNO')
carro1.setAno(2022)
carro1.setModelo('novo')
carro1.info()'''

