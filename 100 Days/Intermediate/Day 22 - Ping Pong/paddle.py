from turtle import Turtle

MOVE_DISTANCE = 40
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.penup()
        self.setheading(90)
        self.color("white")
        self.setposition(position)

    def up(self):
        self.setheading(UP)
        if self.ycor() < 255:
            self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        if self.ycor() > -255:
            self.forward(MOVE_DISTANCE)
