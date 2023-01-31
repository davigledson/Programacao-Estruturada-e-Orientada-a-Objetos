from tkinter import *
janela=Tk()
rot1=Label(janela,text='Valor 1:').grid(row=0,column=0)
campo1= Entry(janela)
campo1.grid(row=0,column=1)

rot2 =Label(janela,text='Valor 2:').grid(row=1,column=0)
campo2= Entry(janela)
campo2.grid(row=1,column=1)

rot3 =Label(janela,text='Total =').grid(row=3,column=0)
campo3= Entry(janela)
campo3.grid(row=3,column=1)

def somar():
    v1=int(campo1.get())
    v2=int(campo2.get())
    total=v1+v2
    campo3.delete(0,END)
    campo3.insert(0,total)

bot=Button(janela,text='Somar',command=somar).grid(row=2,column=1)

mainloop()