from turtle import Turtle, Screen, colormode, mode
import random

tim = Turtle()
tim.shape("turtle")
colormode(255)
mode("standard")
tim.speed("fastest")


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


def drawing_spirograph(offset_gap):
    offset = 0.0
    while offset <= 360:
        tim.pencolor(random_color())
        tim.setheading(offset)
        tim.circle(100)
        offset += offset_gap


drawing_spirograph(24)

screen = Screen()
screen.exitonclick()
