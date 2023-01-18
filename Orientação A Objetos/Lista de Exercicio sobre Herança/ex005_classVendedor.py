from ex003_classEmpregado import Empregado

class Vendedor(Empregado):

    def __init__(self,nome,salario,percentualComissao):
        super().__init__(nome,salario)

        self.percentualComissao=percentualComissao

    def setPercentualComissao(self, percentualComissao):
        self.percentualComissao = percentualComissao

    def getPercentualComissao(self):
        return self.percentualComissao

    def calcularSalario(self):
        return  self.percentualComissao+self.getSalario()

    def info(self):
        super(Vendedor, self).info()
        print('Percentual de comissão:',self.percentualComissao)
        print('Salario Total:',self.calcularSalario())



vendedor1=Vendedor('davi',6000,1000)
vendedor1.setPercentualComissao(500)
#vendedor1.percentualComissao=100 vai assim tbm

vendedor1.info()

