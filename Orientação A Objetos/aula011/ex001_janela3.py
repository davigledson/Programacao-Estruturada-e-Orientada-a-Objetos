from tkinter import *
from  tkinter import messagebox #se não fizer assim vai dar erro
janela = Tk()
janela.title('Boas vindas')
janela.geometry('300x200+100+100')
rot = Label(janela, text="Qual é seu nome?")
rot.grid(row=0,column=0)

campo = Entry(janela)
campo.grid(row=1,column=0)

def bemvindo():

    nome=campo.get()
    msg =f'Seja bem vindo, {nome}!'

    messagebox.showinfo(message=msg)

bot = Button(janela, text='Confirmar',command=bemvindo)
bot.grid(row=2,column=0)

janela.mainloop()