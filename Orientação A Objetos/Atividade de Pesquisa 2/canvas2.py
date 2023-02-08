from tkinter import *

root = Tk()

C = Canvas(root, bg="yellow",
           height=250, width=300)

line = C.create_line(108, 120,
                     320, 40,
                     fill="green")

arc = C.create_arc(180, 150, 80,
                   210, start=0,
                   extent=220,
                   fill="red")

oval = C.create_oval(80, 30, 140,
                     150,
                     fill="blue")

C.pack()
mainloop()