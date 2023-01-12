from ex001_classPessoa_v4 import Pessoa


class Aluno(Pessoa):
    __curso = None

    def setCurso(self, curso):
        self.__curso = curso

    def getCurso(self):
        return self.__curso


aluno1 = Aluno()
aluno1.setNome('Davi')  # da classe pai
aluno1.setIdade(19)  # da classe pai
aluno1.setCurso('Informativa')  # da classe filho

print(aluno1.getNome())  # da classe pai
print(aluno1.getIdade())  # da classe pai
print(aluno1.getCurso())  # da classe filho
