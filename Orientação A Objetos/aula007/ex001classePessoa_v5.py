class Pessoa:
    __nome=None
    __idade=None

    def __init__(self,nome,idade):
        self.__nome = nome
        self.__idade = idade

    def Pessoa(self):
        pass
    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return  self.__nome

    def setIdade(self, idade):
        self.__idade = idade

    def getIdade(self):
        return self.__idade

    def info(self):
        print('Nome =', self.__nome)
        print('Idade =',self.__idade)

