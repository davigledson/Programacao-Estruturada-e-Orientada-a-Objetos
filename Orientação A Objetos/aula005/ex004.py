class FuncionarioEmpresa():
    __nome='davi'
    __setor = 'Banco de Dados'
    __salario = 8000

    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome = nome


    def getSetor(self):
        return self.__setor

    def setSetor(self,setor):
        self.__setor = setor


    def getSalario(self):
        return self.__salario

    def setSalario(self,salario):
       self.__salario =salario

f1=FuncionarioEmpresa()

f1.setNome('Gledson')
f1.setSetor('ADM')

f1.setSalario(10000)
print(f'Sou {f1.getNome()} e trabalho no setor de {f1.getSetor()} e ganho {f1.getSalario()} reais')