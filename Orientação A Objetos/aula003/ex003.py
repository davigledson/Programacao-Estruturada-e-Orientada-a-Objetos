import math


class Circulo():
    import math
    r = 0

    def __init__(self,r):
        if r<0:
            self.raio * -1
        else:
         self.raio=r

    def diametro(self):
        print(f'Diametro ={self.raio *2}')
    def area(self):
        print(f'Area ={math.pi * self.raio ** 2}')

    def circunferencia(self):
        print(f'Circunferencia ={2 * self.raio * math.pi}')


    def info(self):
         print(self.raio)


cir=Circulo(10)
cir.area()
cir.diametro()
cir.circunferencia()
cir.info()
