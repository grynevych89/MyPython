from tkinter import Tk, PhotoImage, Label, Entry, Frame, Button, END
from time import strftime
from tkinter import messagebox
from os import system


# Главное окно:
root = Tk()
root.title("Часы-Будильник")
root.resizable(False, False)
root.config(bg="black")


# Логотип:
img = PhotoImage(file='clock.png')
img = img.subsample(2, 2)
logo = Label(root, bg='black', image=img)
logo.pack(side='left', padx=15, pady=15)


# Циферблат:
clock = Label(root)
clock.config(bg="black", fg='lime', font='Arial 50', text='00:00:00')
clock.pack(padx=20, pady=20)


# Поле установки будильника:
alarm = Entry(root)
alarm.config(fg='red', font='Arial 20', text='не установлен', justify='center', width=10)
alarm.pack()


# Панель для кнопок управления:
panel = Frame(root)
panel.config(bg='black')
panel.pack(pady=20)


# Кнопка включения будильника:
start = Button(panel)
start.config(text='Включить будильник', width=20)
start.pack(side='left')


# Кнопка включения будильника:
stop = Button(panel)
stop.config(text='Выключить будильник', width=20)
stop.pack(padx=10)


# Глобальные переменные:
set_time = 'undefined'


# Функция отображения хода времени:
def tick():
    current_time = strftime('%H:%M:%S')
    clock.config(text=current_time)
    if current_time == set_time:
        # messagebox.showerror('Внимание!!!', 'Ваше время истекло!')
        system('alarm.mp3')
    clock.after(1000, tick)


# Функция включения будильника:
def start_alarm(event):
    global set_time
    set_time = alarm.get()
    messagebox.showinfo('Сообщение', f'Будильник включен на {set_time}')


# Функция выключения будильника:
def stop_alarm(event):
    global set_time
    set_time = 'undefined'
    alarm.delete(0, END)
    messagebox.showwarning('Сообщение', 'Будильник выключен')


# Запуск программы:
tick()
start.bind('<Button-1>', start_alarm)
stop.bind('<Button-1>', stop_alarm)
root.mainloop()
