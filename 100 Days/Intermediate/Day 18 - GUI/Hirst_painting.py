import colorgram
from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
colormode(255)
tim.speed("fastest")
imported_colors = colorgram.extract('images/image.jpg', 20)


class Rgb:

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


colors_list = []

for color in imported_colors:
    rgb = color.rgb
    color_red = rgb.r
    color_green = rgb.g
    color_blue = rgb.b
    color = (color_red, color_green, color_blue)
    colors_list.append(color)


def hirst_painter(picture_size, radius, offset, colors):
    """
    Function to draw a masterpiece of circles having the same diameter and offset but different colors.
    :param picture_size: Number of circles in the line and in column.
    :param radius: Defines size of the circle.
    :param offset: Distance between the circles.
    :param colors: Colors to be used in painting
    :return: None
    """
    y = -480
    tim.penup()
    tim.setposition(-480, y)
    for _ in range(picture_size):
        for _ in range(picture_size):
            tim.fillcolor(random.choice(colors))
            tim.begin_fill()
            tim.circle(radius)
            tim.end_fill()
            tim.penup()
            tim.forward(radius * 2 + offset)
        y += (radius * 2 + offset)
        tim.setposition(-480, y)
    tim.hideturtle()


hirst_painter(picture_size=12, radius=40, offset=17, colors=colors_list)
screen = Screen()
screen.exitonclick()