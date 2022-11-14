import turtle
from random import randint
from time import sleep

turtle.bgcolor("black")

turtle.speed(0)
turtle.pensize(2)

# Drawing a dotted swquare
turtle.pencolor("red")
for k in range(4):
    for j in range(4):
        for i in range(50):
            turtle.penup()
            turtle.forward(5)
            turtle.pendown()
            turtle.forward(1)
        turtle.right(90)
    turtle.right(90)

turtle.clear()

# Drawing circles
turtle.pencolor("blue")
side = 12.5
for i in range(4):
    turtle.circle(side) # this creates a circle of radius = side
    turtle.circle(side*2)
    turtle.circle(side*3)
    turtle.circle(side*4)
    turtle.left(90)

# Drawing a spiral.
side = 800

turtle.penup()
turtle.goto(-side/2,-side/2)
turtle.pendown()

for i in range(160):
    side -= 5
    turtle.forward(side)
    turtle.left(90)
    if i > 150:
        turtle.speed(1)
    
for i in range(50):
    turtle.penup()
    turtle.goto(0,-(10 * i))
    turtle.pendown()
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    turtle.colormode(255)
    turtle.color(r, g, b)
    turtle.circle(10 * i)


#Drawing a squared spiral pattern rotating
side = 2

for i in range(100):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    turtle.colormode(255)  # This allows the color function to take three parameters for Red, Blue and Green
    turtle.color(r, g, b)

    turtle.forward(side)
    turtle.left(92)

    side += 5