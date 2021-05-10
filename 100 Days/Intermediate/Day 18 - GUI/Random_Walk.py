from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
tim.speed("fast")
colormode(255)


def random_walk(distance, angle):
    tim.forward(distance)
    tim.right(angle)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


for x in range(200):
    angles = random.randint(0, 360)
    tim.pensize(x * 0.05)
    tim.pencolor(random_color())
    random_walk(30, angles)


screen = Screen()
screen.exitonclick()
