import tkinter as tk

count = 0


def say_hello():
    print('Hello!')


def add_label():
    label = tk.Label(win, text='Label')
    label.pack()


def counter():
    global count
    count += 1
    btn4['text'] = f'Counter: {count}'


win = tk.Tk()
win.geometry('400x500+100+200')
win.title('Графическое приложение №Ы')

btn1 = tk.Button(win, text='Say Hello',  # создаём кнопку
                 # command=функция,  # действия кнопки
                 command=say_hello
                 )

btn2 = tk.Button(win, text='Add Label',
                 command=add_label
                 )

btn3 = tk.Button(win, text='Add Label (lambda)',
                 command=lambda: tk.Label(win, text='lambda Label').pack()
                 )

btn4 = tk.Button(win, text=f'Counter: {count}',
                 command=counter,
                 activebackground='lightblue',  # цвет при наведении и нажатии
                 bg='lightgreen',
                 state=tk.NORMAL  # состояние - DISABLED (выключена), по умолчанию - NORMAL (включена)
                 )

btn1.pack()  # располагаем на экране
btn2.pack()
btn3.pack()
btn4.pack()

win.mainloop()
