# Classe - Descrição de um item contendo seus atributos e funcionalidades
# Objeto - É a materialização da classe, o item propriamente dito

class minhaClasse:
    idade = 5
    nome='ana'


print(minhaClasse())
print(minhaClasse)
print(minhaClasse.idade)
print(minhaClasse.nome)

print('-'*20)

objeto1=minhaClasse()
print(objeto1.nome)
print(objeto1.idade)

print('-'*20)

objeto1.nome='ana clara'
objeto1.idade=6
print(objeto1.nome)
print(objeto1.idade)