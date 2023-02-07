from tkinter import *
janela =Tk()
janela.geometry('200x50')
def nova():
    janela2=Toplevel(janela)
    janela2.geometry('300x300')
    rot=Label(janela2,text='Essa é a nova janela')
    rot.pack()
    janela.withdraw()



botao = Button(janela,text='Nova',command=nova).pack()

janela.mainloop()
#deu errado