class Empregado:
    __nome=None
    __salario=0.0

    def __init__(self,nome,salario):
        self.__nome=nome
        self.__salario=salario

    def setNome(self,nome):
        self.__nome=nome

    def getNome(self):
        return self.__nome

    def setSalario(self,salario):
        self.__salario=salario

    def getSalario(self):
        return self.__salario

    def info(self):
        print('Nome: ', self.__nome)
        print('Salário: ', self.__salario)

p1=Empregado('davi',8000)
#p1.setNome ='davi'
#p1.setSalario=8000 não roda o info assim por causa o init

p1.info()


