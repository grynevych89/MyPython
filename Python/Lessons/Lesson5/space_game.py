from tkinter import *
from random import *


root = Tk()
root.title("Охота на пришельцев")
root.geometry('800x500+1000+300')
root.config(bg='black')


canvas = Canvas(root)
canvas.config(width=800, height=500, bg='black')
canvas.pack()


n = 1001
for k in range(n):
    x = randint(0, 795)
    y = randint(0, 495)
    canvas.create_oval(x, y, x + 0.1, y + 0.1, outline='white', fill='white')


root.mainloop()
