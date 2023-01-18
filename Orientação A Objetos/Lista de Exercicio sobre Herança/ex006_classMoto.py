from ex004_classTransporte import Transporte
class Moto(Transporte):

    def __init__(self, fabricante, ano, modelo, cilindradas):
        super().__init__(fabricante, ano, modelo)
        self.cilindradas = cilindradas

    def setCilindradas(self, cilindradas):
        self.cilindradas = cilindradas

    def getCilindradas(self):
        return self.cilindradas

    def empinarRoda(self):
        print('Roda dianteira foi erguida')

    def info(self):
        super().info()
        print('Cilindradas:',self.cilindradas)

moto1=Moto('Honda',2020,'novo',3000)
moto1.setCilindradas(200)
moto1.info()
moto1.empinarRoda()


