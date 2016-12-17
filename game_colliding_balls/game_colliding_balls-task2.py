import tkinter

"""
Task1. Мы будем использовать библиотеки tkinter и random. Создадим окно, определим канву, научимся перехватывать события от мыши.
Task2. Создадим основной игровой объект — цветной шарик. Заставим его появляться на месте щелчка мышью.
"""
# constants
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'


# balls class
class Balls():
    def __init__(self, x, y, r, color, dx=0, dy=0):  # координаты, радиус, цвет, смещение
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self): # рисуем круглый овал
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color)  # координаты левого верхнего угла и правого нижнего угла

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=BG_COLOR, outline=BG_COLOR)


# mouse event
def mouse_click(event):
    global main_ball
    if event.num == 1:
        main_ball = Balls(event.x, event.y, 30, 'blue')
        main_ball.draw()
    else:
        main_ball.hide()


root = tkinter.Tk()  # создаем корневое окно
root.title("Colliding Balls")  # Заголовок корневого окна

canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)  # Создаем канву (рабочую поверхность, указываем ее ширину-высоту
canvas.pack()   # отрисовать канву
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')

root.mainloop() # отобразить окно
