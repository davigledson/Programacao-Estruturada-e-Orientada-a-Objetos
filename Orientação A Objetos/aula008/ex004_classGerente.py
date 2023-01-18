from ex003_classEmpregado import Empregado


class Gerente(Empregado):
    departamento = ''

    def __int__(self, departamento):
        self.departamento = departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def getDepartamento(self):
        return self.departamento

    def info(self):

        super(Gerente, self).info()
        print('Departamento:', self.departamento)




pessoa1 = Gerente('davi',8000)
pessoa1.setDepartamento('Desenvolvimento')
pessoa1.info()



