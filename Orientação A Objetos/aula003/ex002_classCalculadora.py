class Calculadora:
    valor1=0
    valor2=0

    def __init__(self,v1,v2):
        self.valor1=v1
        self.valor2=v2

    def digitar(self):
        try:
            self.valor1=int(input('valor 1?'))
            self.valor2 =int(input('valor 2?'))
            print('Valores armazenados com sucesso')
        except (TypeError,ValueError):
            print('Digite apenas numeros!')

    def somar(self):
        v1=self.valor1
        v2=self.valor2
        print(v1+v2)


    def dividir(self):
        try:
            v1 = self.valor1
            v2 = self.valor2
            print(v1/v2)
        except ZeroDivisionError:
            print('Impossivel dividir por zero')

    def imprimir(self):
        v1 = self.valor1
        v2 = self.valor2
        print(f'Valor 1 = {v1}')
        print(f'Valor 2 = {v2}')

calc=Calculadora('a',5)
calc.digitar()
calc.imprimir()