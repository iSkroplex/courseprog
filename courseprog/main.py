from turtle import *
from tkinter import *


# Функция рисующая фрактал
def koch_pain(long, iteration):
    if iteration == 0:
        forward(long)
    else:
        koch_pain(long / 3, iteration - 1)
        left(60)
        koch_pain(long / 3, iteration - 1)
        right(120)
        koch_pain(long / 3, iteration - 1)
        left(60)
        koch_pain(long / 3, iteration - 1)


# Функция кнопки, а также вызов функции которая настраивает рисование фрак-тала
def draw_koch():
    speed_ = speed_turtle.get()
    iteration_ = iteration.get()
    long_ = long.get()
    color_ = color_pen.get()
    draw_koch_snowflake(long_, iteration_, speed_, color_)


# Создание диалогового окна
root = Tk()
root.title("Параметры для построения кривой Коха")
root.geometry("400x300")

# Определение переменных полей для ввода
speed_turtle = IntVar()
iteration = IntVar()
long = IntVar()
color_pen = StringVar()

# Создание названий полей
speed_turtle_label = Label(text="Скорость рисования:")
iteration_label = Label(text="Глубина фрактала:")
long_label = Label(text="Размер линий:")
color_pen_label = Label(text="Цвет линий:")

# Настройка(согласно сетке) названий полей для ввода
speed_turtle_label.grid(row=0, column=1, sticky="w")
iteration_label.grid(row=5, column=1, sticky="w")
long_label.grid(row=6, column=1, sticky="w")
color_pen_label.grid(row=7, column=1, sticky="w")

# Создание полей для ввода
speed_turtle_fastest = Radiobutton(text="Самая быстрая", value=0, variable=speed_turtle, padx=15, pady=0)
speed_turtle_fast = Radiobutton(text="Быстрая", value=10, variable=speed_turtle, padx=15, pady=0)
speed_turtle_normal = Radiobutton(text="Нормальная", value=6, variable=speed_turtle, padx=15, pady=0)
speed_turtle_slow = Radiobutton(text="Медленная", value=3, variable=speed_turtle, padx=15, pady=0)
speed_turtle_slowest = Radiobutton(text="Самая медленная", value=1, variable=speed_turtle, padx=15, pady=0)
iteration_entry = Entry(textvariable=iteration)
long_entry = Entry(textvariable=long)
color_pen_entry = Entry(textvariable=color_pen)

# Настраивание полей для ввода согласно сетке
speed_turtle_fastest.grid(row=0, column=7, padx=5, pady=5, sticky="w")
speed_turtle_fast.grid(row=1, column=7, padx=5, pady=5, sticky="w")
speed_turtle_normal.grid(row=2, column=7, padx=5, pady=5, sticky="w")
speed_turtle_slow.grid(row=3, column=7, padx=5, pady=5, sticky="w")
speed_turtle_slowest.grid(row=4, column=7, padx=5, pady=5, sticky="w")
iteration_entry.grid(row=5, column=7, padx=5, pady=5)
long_entry.grid(row=6, column=7, padx=5, pady=5)
color_pen_entry.grid(row=7, column=7, padx=5, pady=5)

# Очищение полей
iteration_entry.delete(0, END)
long_entry.delete(0, END)
color_pen_entry.delete(0, END)

# Установление значений по умолчанию
iteration_entry.insert(0, 1)
long_entry.insert(0, 300)
color_pen_entry.insert(0, "red")

# Создание и настройка(по сетке) кнопки
message_button = Button(text="Ввести", command=draw_koch)
message_button.grid(row=8, column=7, padx=5, pady=5, sticky="e")

# Функция настройки рисования фрактала и вызов функции рисования
def draw_koch_snowflake(long, iteration, speed_turtle, color_pen):
    root.destroy()
    # Очитска поля
    clear()
    # Установка стандартного цвета
    color("white")
    home()
    # Позицианирование черепашки
    setx(-long / 2)
    sety(long / 3)

    for i in range(3):
        speed(speed_turtle)
        color(color_pen)

        koch_pain(long, iteration)

        right(120)

root.mainloop()
done()
