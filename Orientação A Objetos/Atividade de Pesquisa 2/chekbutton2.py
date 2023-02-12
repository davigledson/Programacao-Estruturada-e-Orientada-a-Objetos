import tkinter as tk

janela = tk.Tk()
var1 = tk.StringVar()
rb1 = tk.Radiobutton(janela, text="Opção 1", variable=var1, value="opção 1", indicatoron=0, selectcolor="blue")
rb1.pack()
rb2 = tk.Radiobutton(janela, text="Opção 2", variable=var1, value="opção 2", indicatoron=0, selectcolor="red")
rb2.pack()

# Verifica o estado do botão de rádio
print("Opção selecionada:", var1.get())

janela.mainloop()
