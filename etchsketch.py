import turtle
from turtle import *

def green():
    turtle.pencolor("green")

def blue():
    turtle.pencolor("blue")

def red():
    turtle.pencolor("red")

def Orchid():
    turtle.pencolor("Medium Orchid")

def up():
    setheading(90)
    forward(100)

def right():
    setheading(0)
    forward(100)

def down():
    setheading(270)
    forward(100)

def left():
    setheading(180)
    forward(100)

def north_e():
    setheading(45)
    forward(100)

def south_e():
    setheading(315)
    forward(100)

def south_w():
    setheading(225)
    forward(100)

def north_w():
    setheading(135)
    forward(100)

listen()

onkey(up, 'Up')
onkey(down, 'Down')
onkey(right, 'Right')
onkey(left, 'Left')

onkey(up, 'w')
onkey(down, 's')
onkey(left, 'a')
onkey(right, 'd')

onkey(north_e, 'e')
onkey(north_w,'q')
onkey(south_e,'c')
onkey(south_w,'z')

onkey(green, '1')
onkey(blue, '2')
onkey(red, '3')
onkey(Orchid, '4')
