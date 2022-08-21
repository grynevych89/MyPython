from tkinter import *


def clicked():
    text.configure(text=quit())


# Главное окно:
root = Tk()
root.title("Визитка")
root.resizable(False, False)
root.config(bg="White")


# Меню:
menu = Menu(root)
new_item = Menu(menu, tearoff=0)
new_item.add_command(label='Выход', command=quit)
menu.add_cascade(label='Файл', menu=new_item)
root.config(menu=menu)


# Фото
img = PhotoImage(file='profile.png')
img = img.subsample(7, 7)
logo = Label(root, bg='Black', image=img)
logo.pack(padx=1, pady=1)


# Содержимое:
about = (
    '\nФамилия: Гриневич'
    '\nИмя: Николай'
    '\nОтчество: Александрович'
    '\nВозраст: 32 года'
    '\nПроживает: г. Киев'
    '\nРабота: Эпицентр-К'
    '\nДолжность: Продавец-консультант'
    '\nНазвание учебного заведения: Компьютерная Академия "ШАГ"'
    '\nКурсы: Изучает язык програмирования Python'
)
text = Label(bg='White', font=("Arial Bold", 16), text=about)
text.pack()


# Кнопка
button = Button(text='Закрыть', bg='White', fg='Black', command=clicked)
button.pack()


root.mainloop()
