from ex004_classTransporte import Transporte
class Moto(Transporte):

    def __init__(self, fabricante, ano, modelo, cilindrada):
        super().__init__(fabricante, ano, modelo)
        self.cilindrada = cilindrada




