# ptitulo = variavel com parametro
class Livro():
    def __init__(self, ptitulo, pautor, pano):
        self.titulo =ptitulo
        self.autor=pautor
        self.ano=pano
        self.pagina=1

    def info(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano: {self.ano}')
        print(f'Pagina atual:{self.pagina}\n')

    def passaPagina(self):
        self.pagina +=1

    def voltaPagina(self):
        if self.pagina >1:
            self.pagina -= 1

livro4=Livro('O Hobbit','J.R.R. Tolkien',1949)
livro4.info()

livro4.passaPagina()


livro4.voltaPagina()
livro4.voltaPagina()


for x in range(10):
    livro4.passaPagina()
livro4.info()