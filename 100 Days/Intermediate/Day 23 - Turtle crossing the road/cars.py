from turtle import Turtle

MOVE_DISTANCE = 40


class Car(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.setheading(180)
        self.color(color)
        self.setposition(position)

    def move(self):
        self.forward(MOVE_DISTANCE)
