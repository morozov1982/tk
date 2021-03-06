import tkinter as tk  # импортируем

win = tk.Tk()  # создаём главное окно

icon = tk.PhotoImage(file='fun.png')  # подгружаем картинку
win.iconphoto(False, icon)  # меняем иконку основного окна

win.config(bg='#CCFFCC')  # цвет фона окна

win.title('Графическое приложение №Ы')  # меняем заголовок главного окна
win.geometry('500x600+1000+300')  # меняем размеры окна (ширина, длина, положение по x и y относительно экрана)
win.minsize(300, 400)  # минимальный размер окна
win.maxsize(700, 800)  # максимальный размер окна
win.resizable(False, False)  # запрещаем/разрешаем ресайз (ширина, высота) (по умолчанию: True, True)
win.mainloop()  # запускаем главный цикл
