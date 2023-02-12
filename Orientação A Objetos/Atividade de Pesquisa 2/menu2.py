import tkinter as tk

janela = tk.Tk()
barra_menu = tk.Menu(janela)

# Adiciona um item de menu
item_arquivo = tk.Menu(barra_menu, tearoff=0)
item_arquivo.add_command(label="Abrir")
item_arquivo.add_command(label="Salvar")
item_arquivo.add_separator()
item_arquivo.add_command(label="Sair")
barra_menu.add_cascade(label="Arquivo", menu=item_arquivo)

# Adiciona outro item de menu
item_editar = tk.Menu(barra_menu, tearoff=0)
item_editar.add_command(label="Copiar")
item_editar.add_command(label="Colar")
barra_menu.add_cascade(label="Editar", menu=item_editar)

janela.config(menu=barra_menu)
janela.mainloop()