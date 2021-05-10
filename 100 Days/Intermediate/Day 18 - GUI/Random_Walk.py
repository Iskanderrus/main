from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.speed("fast")


def random_walk(distance, angle, turtle_color):
    tim.forward(distance)
    tim.right(angle)
    tim.color(turtle_color)


angles = [0, 90, 180, 270]

colors = ["red", "blue", "orange", "black", "green", "gray", "gold", "lime", "deep sky blue", "magenta"]
for x in range(200):
    tim.width(x * 0.05)
    random_walk(30, random.choice(angles), random.choice(colors))

screen = Screen()
screen.exitonclick()
