from turtle import Turtle, Screen
from random import choice


tim = Turtle()
tim.shape("turtle")


def figure(distance, angle, side, turtle_color):
    for _ in range(side):
        tim.forward(distance)
        tim.right(angle)
        tim.color(turtle_color)


def dashed_line():
    for _ in range(15):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)


tim.position = [10, 10, 10]
sides = 3
angles = [60, 90, 108, 120, 128.571, 135, 140, 144]
a = 0
colors = ["red", "blue", "orange", "black", "green", "gray", "gold", "lime", "deep sky blue", "magenta"]
while sides < 10:
    color = choice(colors)
    figure(100, (180 - angles[a]), sides, color)
    sides += 1
    a += 1

screen = Screen()
screen.exitonclick()
