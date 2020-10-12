import tkinter as tk


win = tk.Tk()
win.geometry('400x500+100+200')
win.title('Графическое приложение №Ы')

btn1 = tk.Button(win, text='Hello 1')
btn2 = tk.Button(win, text='Hello 2')
btn3 = tk.Button(win, text='Hello 3')
btn4 = tk.Button(win, text='Hello world 4')
btn5 = tk.Button(win, text='Hello 5')
btn6 = tk.Button(win, text='Hello 6')
btn7 = tk.Button(win, text='Hello 7')
btn8 = tk.Button(win, text='Hello 8')

# помогает располагать виджеты в виде таблицы
btn1.grid(row=0, column=0)  # ряд, колонка (столбец)
btn2.grid(row=0, column=1, stick='w')  # прижимает влево
btn3.grid(row=1, column=0, stick='we')  # притягивает содержимое (w - к левому краю, e - к правому), т. е. растягивает
btn4.grid(row=1, column=1)
btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1, stick='e')  # прижимает вправо
btn7.grid(row=3, column=0, columnspan=2, stick='we')  # columnspan - объединяет ячейки по ширине
btn8.grid(row=0, column=2,
          rowspan=4,  # объединяет ячейки по высоте
          stick='ns'  # притягивает содержимое (n - к верхнему краю, s - к нижнему), т. е. растягивает
          )

win.grid_columnconfigure(0,  # настраивает 0 солонку
                         minsize=150  # минимальная ширина - 150px
                         )
win.grid_columnconfigure(1, minsize=150)

win.mainloop()
