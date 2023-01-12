class Inimigo:
    def __init__(self):
        self.nome='Malvadão'
        self.__vida=10

    def verVida(self): # para poder ver a vida
        print(self.__vida)

    def menosVida(self):
        self.__vida-=2
        if self.__vida <=0:
            self.__morreu()

    def __morreu(self):

        if self.__vida <= 0:
            print('Morreu')

in1= Inimigo()
print(in1.nome)
in1.verVida()
in1.menosVida()
in1.verVida()
in1.menosVida()


for c in range(3):
    in1.menosVida()
in1.verVida()