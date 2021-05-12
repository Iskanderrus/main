from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
colormode(255)
tim.speed("fastest")


def random_color():
    """
    Function to generate random color in RGB format.
    return: color
    """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


def picasso_painter(picture_size, radius, offset):
    """
    Function to draw a masterpiece of circles having the same diameter and offset but different colors.
    :param picture_size: Number of circles in the line and in column.
    :param radius: Defines size of the circle.
    :param offset: Distance between the circles. 
    :return: None
    """
    y = -480
    tim.penup()
    tim.setposition(-480, y)
    for _ in range(picture_size):
        for _ in range(picture_size):
            tim.fillcolor(random_color())
            tim.begin_fill()
            tim.circle(radius)
            tim.end_fill()
            tim.penup()
            tim.forward(radius * 2 + offset)
        y += (radius * 2 + offset)
        tim.setposition(-480, y)
    tim.hideturtle()


picasso_painter(picture_size=10, radius=15, offset=7)
screen = Screen()
screen.exitonclick()
