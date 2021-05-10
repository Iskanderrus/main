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


circle_step = 0.0

while circle_step < 360:
    tim.pencolor(random_color())
    tim.setheading(circle_step)
    tim.circle(100)
    circle_step += 5

screen = Screen()
screen.exitonclick()
