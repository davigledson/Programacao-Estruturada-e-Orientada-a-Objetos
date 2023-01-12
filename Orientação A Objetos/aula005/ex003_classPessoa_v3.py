class Pessoa:
    __idade = 19
    __nome='Carlos'
    def getIdade(self):
        return self.__idade

    def setIdade(self,idade):
        if idade<0:
            idade=idade* -1
        self.__idade=idade


    def getNome(self):
        return self.__nome

    def setNome(self,nome):
         self.__nome = nome

p1=Pessoa()
p1.setIdade(20)
p1.setNome('Davi')
print(p1.getIdade())

p1.setIdade(-25)
print(p1.getIdade())



print(f'Sou {p1.getNome()} e eu tenho {p1.getIdade()} anos ')