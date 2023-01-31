from tkinter import *
from  tkinter import messagebox #se não fizer assim vai dar erro
janela=Tk()
rot1=Label(janela,text='Valor 1:')
rot1.grid(row=0,column=0)
campo1=Entry(janela)
campo1.grid(row=0,column=1)

rot2=Label(janela,text='Valor 2:')
rot2.grid(row=1,column=0)
campo2=Entry(janela)
campo2.grid(row=1,column=1)

def somar():
    v1=int(campo1.get())
    v2=int(campo2.get())

    frase =f'Soma = {v1+v2}'
    messagebox.showinfo(message=frase)

def multiplicar():
    v1=int(campo1.get())
    v2=int(campo2.get())

    frase=f'Multiplicação = {v1*v2}'
    messagebox.showinfo(message=frase)

def subtrair():
    v1=int(campo1.get())
    v2=int(campo2.get())

    frase=f'Multiplicação = {v1-v2}'
    messagebox.showinfo(message=frase)

bot = Button(janela,text='Somar',command=somar,width=12)
bot.grid(row=2,column=1)

bot2 = Button(janela,text='Multiplicar',command=multiplicar,width=12)
bot2.grid(row=3,column=1)

bot3 = Button(janela,text='Subtrair',command=subtrair,width=12)
bot3.grid(row=4,column=1)
janela.mainloop()