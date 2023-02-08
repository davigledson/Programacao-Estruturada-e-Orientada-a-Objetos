from tkinter import *

class TelaDesenho(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_line)

    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def add_line(self, event):
        self.create_line((self.lastx, self.lasty, event.x, event.y))
        self.save_posn(event)


janela = Tk()
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)

sketch = TelaDesenho(janela)
sketch.grid(column=0, row=0, )

janela.mainloop()
