import turtle
from random import randint

turtle.bgcolor("black")

turtle.speed(0)
turtle.pensize(2)

side = 5

for i in range(500):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    turtle.colormode(255)
    turtle.color(r, g, b)

    turtle.forward(side)
    turtle.left(92)

    side += 2

