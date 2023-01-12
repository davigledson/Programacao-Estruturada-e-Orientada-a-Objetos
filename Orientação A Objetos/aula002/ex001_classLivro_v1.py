class Livro():
    titulo=''
    autor = ''
    ano = ''

livro1=Livro()

livro1.titulo='O cavalheiros dos 7 reinos'
livro1.ano='2018'
livro1.autor='J.J martin'

livro2=Livro()
livro2.titulo='Python para zumbis'
livro2.autor='Jose Morreu'
livro2.ano ='2021'

print(f'Eu tenho livros de {livro1.autor} e {livro2.autor}')