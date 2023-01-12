from ex001classePessoa_v5 import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, salario, formacao):
        super().__init__(nome,idade)
        self.__salario =salario
        self.__formacao =formacao



    def setSalario(self,salario):
        self.__salario =salario

    def getSalario(self):
        return self.__salario

    def setFormacao(self,formacao):
        self.__formacao =formacao

    def getFormacao(self):
        return self.__formacao

    def info(self):
        super(Professor, self).info()
        print('Formação =', self.__formacao)
        print('Salario =', self.__salario)


'''
prof1 =Professor()
prof1.setNome('Murilo')
prof1.setIdade(25)
prof1.setSalario(2000)
prof1.setFormacao('Historia')

print(f'prof {prof1.getNome()} ensina {prof1.getFormacao()} com salario de {prof1.getSalario()} reais')

'''

#VAI EXECURA OS CODIGO NO ARQUIVO SEGUINTE

#prof3 = Professor('carla',31,3000,'Biologia')
#print(f'Hoje tem aula de {prof3.getFormacao()} com {prof3.getNome()}')
#prof3.info()