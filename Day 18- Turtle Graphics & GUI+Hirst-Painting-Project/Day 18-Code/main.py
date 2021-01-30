import random
from turtle import *

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.forward(100)
timmy.left(90)

colormode(255)


def random_color():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return (R, G, B)


screen = Screen()
screen.exitonclick()
