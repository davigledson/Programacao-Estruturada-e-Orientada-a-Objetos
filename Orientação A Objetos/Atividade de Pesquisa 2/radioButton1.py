import tkinter as tk

janela = tk.Tk()
var = tk.IntVar()

rb1 = tk.Radiobutton(janela, text="Opção 1", variable=var, value=1)
rb2 = tk.Radiobutton(janela, text="Opção 2", variable=var, value=2)
rb3 = tk.Radiobutton(janela, text="Opção 3", variable=var, value=3)

rb1.pack()
rb2.pack()
rb3.pack()

janela.mainloop()
