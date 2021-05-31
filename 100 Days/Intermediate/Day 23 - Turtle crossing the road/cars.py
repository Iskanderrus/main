from turtle import Turtle, colormode
import random

colormode(255)


class Car(Turtle):

    def __init__(self, y_position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.color(color)
        self.setposition(x=400, y=y_position)

    def move(self):
        self.forward(random.randint(0, 40))
