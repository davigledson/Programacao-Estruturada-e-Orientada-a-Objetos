class Pessoa:

    nome=''
    idade=0
    email=''
    def __init__(self,pnome,pidade,pemail):
        self.email=pemail
        self.nome=pnome
        self.idade=pidade


p1=Pessoa('joao',25,'')
p1.email='davi@gmail.com'
print(p1.nome,p1.idade,p1.email)

p3=Pessoa('carlos',26,'')


#ver o resto do codigo no suap
