import tkinter as tk  # импортируем

win = tk.Tk()
win.geometry('300x400+100+200')
win.title('Графическое приложение №Ы')

label_1 = tk.Label(win, text='Hello!',  # создаём Label
                   bg='red',  # фон текста
                   fg='white',  # цвет текста
                   font=('Arial', 15, 'bold'),  # шрифт
                   padx=20,  # отступы слева и справа
                   pady=40,  # отступы сверху и снизу
                   width=20,  # ширина (в знаках)
                   height=10,  # высота
                   anchor='nw',  # выравнивание текста: center, n - верх, s - низ, w - слева, e - справа (можно парами)
                   relief=tk.RAISED,  # границы
                   bd=10,  # ширина границы
                   justify=tk.CENTER  # выравнивание строк текста: LEFT, RIGHT, JUSTIFY
                   )
label_1.pack()  # располагаем на экране

win.mainloop()
