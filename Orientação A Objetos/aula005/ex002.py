class BombaCombustivel:
    __litros=1000

    def info(self):
        print(f'Restam: {self.__litros} litros.')

    def vender(self,qtd):
        self.__litros -= qtd
        self.__alerta()

    def __alerta(self):
        if self.__litros <= 0:
            print('Tanque Vazio.')

b1=BombaCombustivel()
b1.vender(1000)
b1.info()