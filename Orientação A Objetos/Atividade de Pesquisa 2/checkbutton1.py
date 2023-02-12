import tkinter as tk

janela = tk.Tk()
var1 = tk.BooleanVar()
cb1 = tk.Checkbutton(janela, text="Opção 1", variable=var1)
cb1.pack()
var2 = tk.BooleanVar()
cb2 = tk.Checkbutton(janela, text="Opção 2", variable=var2)
cb2.pack()
var3 = tk.BooleanVar()
cb3 = tk.Checkbutton(janela, text="Opção 3", variable=var3)
cb3.pack()

janela.mainloop()