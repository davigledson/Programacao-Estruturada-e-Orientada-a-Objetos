from ex002classeProfessor import Professor
class Visitante(Professor):
    __instituicao = None

    def __init__(self,nome,idade,salario,formacao,instituicao):
        super().__init__(nome,idade,salario,formacao)
        self.__instituicao =instituicao

    def info(self):
        super().info() # executa o código da classe pai
        print('Instituição =',self.__instituicao)
print('-'*20)
visi1=Visitante('Ana',37,4000,'Física','UERN')
visi1.info()