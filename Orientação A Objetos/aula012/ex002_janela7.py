from tkinter import *
from  tkinter import messagebox
janela = Tk()
janela.geometry('200x120')

rot_usuario=Label(janela,text='Usuário:').pack()

campo_usuario=Entry(janela)
campo_usuario.pack()

rot_senha =Label(janela,text='senha').pack()

campo_senha=Entry(janela, show='*')
campo_senha.pack()

def login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    if usuario =='admin' and senha == 'legal':
        #messagebox.showinfo(message='ACESSO PERMITIDO')
        janela2 = Toplevel(janela)
        janela2.geometry('300x300')
        rot = Label(janela2, text='Essa é a nova janela')
        rot.pack()
        janela.withdraw()
    else:
        messagebox.showinfo(message='ACESSO NEGADO')

botao =Button(janela,text ='Entrar',command=login).pack()

janela.mainloop()