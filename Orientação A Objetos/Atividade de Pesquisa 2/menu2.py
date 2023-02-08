import tkinter as tk

janela = tk.Tk()
barra_menu = tk.Menu(janela)
janela.config(menu=barra_menu)
arquivo_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Arquivo", menu=arquivo_menu)
arquivo_menu.add_command(label="Abrir...")

janela.mainloop()
