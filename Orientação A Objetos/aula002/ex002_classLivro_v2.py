# ptitulo = variavel com parametro
class Livro():
    def __init__(self, ptitulo, pautor, pano):
        self.titulo =ptitulo
        self.autor=pautor
        self.ano=pano

livro3=Livro('1984','George Orwell',1948)

print(f'Você leu {livro3.titulo}? de {livro3.autor} que foi lançado em {livro3.ano}')