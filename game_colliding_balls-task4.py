import tkinter
import random

"""
Task1. Мы будем использовать библиотеки tkinter и random. Создадим окно, определим канву, научимся перехватывать события от мыши.
Task2. Создадим основной игровой объект — цветной шарик. Заставим его появляться на месте щелчка мышью.
Task3. Научим шарик двигаться и отскакивать от краёв экрана. Освоим управление движущимся шариком с помощью мыши.
Task4. Создадим «россыпь» неподвижных шаров, которые наш шарик будет «выбивать». Научимся обрабатывать столкновения.
"""
# constants
WIDTH = 640
HEIGHT = 480
BG_COLOR = 'white'
COLOR = ['aqua', 'fuchsia', 'pink', 'yellow', 'gold', 'chartreuse']
ZERO = 0
MAIN_BALL_RADIUS = 30
MAIN_BALL_COLOR = 'blue'
INIT_DX = 1
INIT_DY = 1
DELAY = 5


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
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color, outline=self.color)  # координаты левого верхнего угла и правого нижнего угла

    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=BG_COLOR, outline=BG_COLOR)

    def is_collision(self, ball): # есть ли столкновение?
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a*a + b*b)**0.5 <= self.r + ball.r


    def move(self):
        # colliding with walls
        # столкновение с вертикальной стеной
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= ZERO):
            self.dx = -self.dx
        # столкновение с горизонтальной стеной
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= ZERO):
            self.dy = -self.dy
        # colliding with balls
        for ball in balls:
            if self.is_collision(ball):
                ball.hide()
                balls.remove(ball)
                self.dx = -self.dx
                self.dy = -self.dy

        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()


# mouse event
def mouse_click(event):
    global main_ball
    if event.num == 1:
        if 'main_ball' not in globals():
            main_ball = Balls(event.x, event.y, MAIN_BALL_RADIUS, MAIN_BALL_COLOR, INIT_DX, INIT_DY)
            main_ball.draw()
        else:  # turn left
            if main_ball.dx * main_ball.dy > ZERO:
                main_ball.dy = -main_ball.dy
            else:
                main_ball.dx = -main_ball.dx
    if event.num == 3: # turn right
        if main_ball.dx * main_ball.dy > ZERO:
            main_ball.dx = -main_ball.dx
        else:
            main_ball.dy = -main_ball.dy
    else:
        main_ball.hide()

# create list of balls
def create_list_of_balls(number):
    lst = []
    while len (lst) < number:
        next_ball = Balls(random.choice(range(0, WIDTH)),  # координата x
                          random.choice(range(0, HEIGHT)),  # координата y
                          random.choice(range(15, 35)),  # диаметр
                          random.choice(COLOR))
        lst.append(next_ball)
        next_ball.draw()
    return lst

# main game cicle
def main():
    if 'main_ball' in globals():
        main_ball.move()
    root.after(DELAY, main)

root = tkinter.Tk()  # создаем корневое окно
root.title("Colliding Balls")  # Заголовок корневого окна
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)  # Создаем канву (рабочую поверхность, указываем ее ширину-высоту
canvas.pack()   # отрисовать канву
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-3>', mouse_click, '+')
if 'main_ball' in globals():
    del main_ball
balls = create_list_of_balls(5)
main()
root.mainloop() # отобразить окно
