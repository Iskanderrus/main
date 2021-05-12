import colorgram
from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
colormode(255)
tim.speed("fastest")
imported_colors = colorgram.extract('images/image.jpg', 20)
colors_list = []
tim.hideturtle()

for color in imported_colors:
    rgb = color.rgb
    color_red = rgb.r
    color_green = rgb.g
    color_blue = rgb.b
    color = (color_red, color_green, color_blue)
    colors_list.append(color)


def hirst_painter(picture_size, dot_size, offset, colors):
    """
    Function to draw a masterpiece of circles having the same diameter and offset but different colors.
    :param picture_size: Number of circles in the line and in column.
    :param dot_size: Defines size of the circle.
    :param offset: Distance between the circles.
    :param colors: Colors to be used in painting
    :return: None
    """
    y = -430
    tim.penup()
    tim.setposition(-390, y)
    for _ in range(picture_size):
        for _ in range(picture_size):
            tim.dot(dot_size, random.choice(colors))
            tim.forward(dot_size + offset)
        y += (dot_size + offset)
        tim.setposition(-390, y)


hirst_painter(picture_size=10, dot_size=40, offset=45, colors=colors_list)
screen = Screen()
screen.exitonclick()
