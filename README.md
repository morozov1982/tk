# Tkinter: информация и примеры

**Установка:**

`sudo apt-get install python3-tk`

## Главное окно

Создаём и запускаем главное окно [lesson1.py](gui_project/lesson1.py)

```Python3
import tkinter as tk  # импортируем

win = tk.Tk()  # создаём главное окно
win.mainloop()  # запускаем главный цикл
```

Размеры и положение окна

```Python3
win.geometry('500x600+10+10')  # размеры окна (ширина, длина, x и y относительно экрана)
win.minsize(300, 400)  # минимальный размер
win.maxsize(700, 800)  # максимальный размер
win.resizable(False, False)  # запрещаем/разрешаем ресайз (ширина, высота)
```

Меняем иконку окна

```Python3
icon = tk.PhotoImage(file='fun.png')  # подгружаем
win.iconphoto(False, icon)  # применяем
```

Цвет фона окна

```Python3
win.config(bg='#CCFFCC')  # RGB
```

## Виджеты

### Label

`Label` - для отображения текстовой информации [lesson2.py](gui_project/lesson2.py)

```Python3
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
```

### Button

`Button` - кнопка [lesson3.py](gui_project/lesson3.py)

```Python3
def say_hello():
    print('Hello!')

btn = tk.Button(win, text='Say Hello',  # создаём кнопку
                 # command=функция,  # действия кнопки
                 command=say_hello,
                 activebackground='lightblue',  # цвет при наведении и нажатии
                 bg='lightgreen',
                 state=tk.NORMAL  # состояние - DISABLED (выключена), по умолчанию - NORMAL (включена)
                 )

btn.pack()  # располагаем на экране
```

```Python3
def add_label():
    label = tk.Label(win, text='Label')
    label.pack()

btn = tk.Button(win, text='Add Label',
                 command=add_label  # по нажатию создаётся метка
                 )
btn.pack()
```

Использование **lambda функций**:

```Python3
btn = tk.Button(win, text='Add Label (lambda)',
                 command=lambda: tk.Label(win, text='lambda Label').pack()
                 )
btn.pack()
```

Использование **счётчика**:

```Python3
count = 0

def counter():
    global count
    count += 1
    btn4['text'] = f'Counter: {count}'

btn = tk.Button(win, text=f'Counter: {count}',
                 command=counter
                 )
btn.pack()
```

### Entry

`Entry` - поле для ввода [lesson5.py](gui_project/lesson5.py)

```Python3
name = tk.Entry(win)  # поле для ввода
name.grid(row=0, column=1)
```

Поле **для ввода пароля**:

```Python3
password = tk.Entry(win, show='*')  # show - скрывает вводимые символы
password.grid(row=1, column=1)
```

```Python3
value = name.get()  # берёт содержимое поля для ввода
name.delete(0, tk.END)  # удаляет содержимое с 0 позиции по tk.END (конец строки, можно написать просто 'end')
name.insert(0, 'Привет!')  # вставляет текст в 0 позицию
```

## Метод grid()

Помогает располагать виджеты в виде таблицы [lesson4.py](gui_project/lesson4.py)

```Python3
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
```

Создаём сетку с использованием цикла for: [lesson4-for.py](gui_project/lesson4-for.py)

```Python3
for i in range(5):  # 5 рядов
    for j in range(2):  # 2 колонки
        tk.Button(win, text=f'Hello {j}-{i}').grid(row=i, column=j, stick='we')

win.grid_columnconfigure(0, minsize=150)
win.grid_columnconfigure(1, minsize=150)
```