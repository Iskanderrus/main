from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90


class Crosser(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("black")
        self.setposition(x=0, y=-380)

    def up(self):
        self.setheading(UP)
        if self.ycor() < 255:
            self.forward(MOVE_DISTANCE)
