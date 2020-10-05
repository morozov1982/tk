# Tkinter: информация и примеры

**Установка:**

```sudo apt-get install python3-tk```

Создаём и запускаем главное окно

```Python3
import tkinter as tk  # импортируем

win = tk.Tk()  # создаём главное окно
win.mainloop()  # запускаем главный цикл
```

Размеры и положение окна

```
win.geometry('500x600+10+10')  # размеры окна (ширина, длина, x и y относительно экрана)
win.minsize(300, 400)  # минимальный размер
win.maxsize(700, 800)  # максимальный размер
win.resizable(False, False)  # запрещаем/разрешаем ресайз (ширина, высота)
```

Меняем иконку окна

```
icon = tk.PhotoImage(file='fun.png')  # подгружаем
win.iconphoto(False, icon)  # применяем
```

Цвет фона окна

```
win.config(bg='#CCFFCC')  # RGB
```