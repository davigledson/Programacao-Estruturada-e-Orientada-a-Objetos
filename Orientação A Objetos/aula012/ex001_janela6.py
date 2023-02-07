from tkinter import *

janela=Tk()

campo1=Entry(janela,fg='RED',bg='yellow', font=('Arial,26,italic'), justify='center', show='*',state='disabled') #state='disabled desativa a digitacao
campo1.grid(row=0,column=0)


def exibir():
    #print(campo1.get())
    if campo1['state']=='disabled':
        campo1['state'] = 'normal'
    else:
        campo1['state'] ='disabled'

botao=Button(janela,text='OK',command=exibir)
botao.grid(row=1,column=0)
janela.mainloop()