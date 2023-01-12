class pessoa:

    def __init__(self, pnome, pidade):
        self.nome = pnome
        self.idade = pidade

#p1=pessoa() dá erro

p1=pessoa('camila',26)
p2=pessoa('kaio',19)

print(f'{p1.nome} tem {p1.idade} anos')
print(f'{p2.nome} tem {p2.idade} anos')

nome3=input('digite o nome:')
idade3=input('digite a idade:')
p3= pessoa(nome3,idade3)
print(f'{p3.nome} tem {p3.idade} anos')
