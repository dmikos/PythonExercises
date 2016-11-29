import tkinter

"""
Task1. Мы будем использовать библиотеки tkinter и random. Создадим окно, определим канву, научимся перехватывать события от мыши.
"""
# constants
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'


# mouse event
def mouse_click(event):
    print(event.num, event.x, event.y) # показать в консоли номер нажатой клавиши и координаты клика мышки


root = tkinter.Tk() # создаем корневое окно
root.title("Colliding Balls")    # Заголовок корневого окна

canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR) # Создаем канву (рабочую поверхность, указываем ее ширину-высоту
canvas.pack()   # отрисовать канву
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')

root.mainloop() # отобразить окно
