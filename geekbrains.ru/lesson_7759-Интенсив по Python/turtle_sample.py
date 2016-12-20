# https://server.179.ru/tasks/python/old/turtle.html

import turtle           # Подключаем модуль turtle

turtle.reset()          # Приводим черепашку в начальное положение
turtle.down()           # Опускаем перо перо (начало рисования)
turtle.forward(200)      # Проползти 20 пикселей вперед
turtle.left(90)         # Поворот влево на 90 градусов
turtle.forward(200)      # Рисуем вторую сторону квадрата
turtle.left(90)
turtle.forward(200)      # Рисуем третью сторону квадрата
turtle.left(90)
turtle.forward(200)      # Рисуем четвертую сторону квадрата
turtle.up()             # Поднять перо (закончить рисовать)
turtle.forward(100)     # Отвести черепашку от рисунка в сторону
# turtle._root.mainloop() # Задержать окно на экране

turtle.pendown()
turtle.circle(30)
turtle.penup()

turtle.goto(150, 200)
turtle.pendown()
turtle.circle(30)
turtle.penup()

turtle.goto(-70, 200)
turtle.pendown()
turtle.circle(30)

input('Press Enter')