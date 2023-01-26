from tkinter import *
janela = Tk()
janela.geometry('400x400+400+200') # vai corta a foto se ela for grande demais
janela.title('programa da nasa')
janela.resizable(FALSE,TRUE) # não deixa altera o tamanho
janela.minsize(300,150)
janela.maxsize(600,350)
texto1 = 'Esse é\n um texto \ncom varias \nlinhas'
rot1 = Label(janela,text = texto1,justify ='left')
rot1.grid(row=0, column =0)

texto2 = """Esse texto 
tambem tem
 varias linhas."""
rot2 = Label(janela,text = texto2,justify ='right')
rot2.grid(row=1,column=1)


imagem = PhotoImage(file='python-logo-2.png')
rot3=Label(janela,image=imagem)
rot3.grid(row=2,column=2)
janela.mainloop()