import ex001_classPessoa_v4
# importado de ex001 da mesma pasta [aula006]

p1=ex001_classPessoa_v4.Pessoa()

p1.setNome('DaviGledson')
p1.setIdade(20)

print(f'Olá {p1.getNome()}')
print(f'Você tem {p1.getIdade()}')