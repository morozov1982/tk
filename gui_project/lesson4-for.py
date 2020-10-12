import tkinter as tk


win = tk.Tk()
win.geometry('400x500+100+200')
win.title('Графическое приложение №Ы')

for i in range(5):  # 5 рядов
    for j in range(2):  # 2 колонки
        tk.Button(win, text=f'Hello {j}-{i}').grid(row=i, column=j, stick='we')

win.grid_columnconfigure(0, minsize=150)
win.grid_columnconfigure(1, minsize=150)

win.mainloop()
