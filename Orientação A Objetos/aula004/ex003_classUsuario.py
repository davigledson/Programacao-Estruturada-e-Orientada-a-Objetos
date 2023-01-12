import getpass

class Usuario:
    def __init__(self,pnome,psenha,):
        self.nome=pnome #public
        self.__senha=psenha #private

    def validar(self,psenha):
        if psenha == self.__senha:
            print('Acesso permitido')

        else:
            print('Acesso negado')

nome=input('Nome:')
senha = getpass.getpass(prompt='Senha:') #bugado no pychan

user1=Usuario(nome,senha)
user1.validar('0')