from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
INITIAL_POSIITION = (0, -280)
FINISH_LINE_Y = 280


class Crosser(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("black")
        self.setposition(INITIAL_POSIITION)

    def up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.setheading(UP)
            self.forward(MOVE_DISTANCE)
        else:
            self.setposition(INITIAL_POSIITION)
