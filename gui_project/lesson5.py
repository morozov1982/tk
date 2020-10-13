import tkinter as tk


def get_entry():
    value = name.get()  # берёт содержимое поля для ввода
    if value:
        print(value)
    else:
        print('Пустота')


def delete_entry():
    name.delete(0, tk.END)  # удаляет содержимое с 0 позиции по tk.END (конец строки, можно написать просто 'end')


def submit():
    print('Имя:', name.get())
    print('Пароль:', password.get())
    delete_entry()
    password.delete(0, tk.END)


win = tk.Tk()
win.geometry('400x500+100+200')
win.title('Графическое приложение №Ы')

tk.Label(win, text='Имя').grid(row=0, column=0, stick='w')
tk.Label(win, text='Пароль').grid(row=1, column=0, stick='w')

name = tk.Entry(win)  # поле для ввода
password = tk.Entry(win, show='*')  # show - скрывает вводимые символы

name.grid(row=0, column=1)
password.grid(row=1, column=1)

tk.Button(win, text='взять', command=get_entry).grid(row=2, column=0, stick='we')
tk.Button(win, text='удалить', command=delete_entry).grid(row=2, column=1, stick='we')
tk.Button(win, text='вставить',
          # вставляет текст в 0 позицию
          command=lambda: name.insert(0, 'Привет!'))\
    .grid(row=2, column=2, stick='we')
tk.Button(win, text='Отправить', command=submit).grid(row=3, column=0, stick='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)

win.mainloop()
