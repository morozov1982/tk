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