from tkinter import *
from time import *


# Главное окно:
root = Tk()
root.config(bg='black')
root.title('Часы-будильник')


# Логотип:
img = PhotoImage(file='logo.png')
img = img.subsample(2, 2)
logo = Label(root, bg='black', image=img)
logo.pack(side='left', padx=15, pady=15)


# Циферблат:
clock = Label(root)
clock.config(bg='black', fg='lime', font='Arial 50', text='00:00:00')
clock.pack(padx=15)


# Функция отображения хода времени:
def tick():
    current = strftime('%H:%M:%S')
    clock.config(text=current)
    clock.after(1000, tick)


# Запуск программы:
tick()
root.mainloop()
