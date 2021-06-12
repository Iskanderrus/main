from turtle import Turtle
import time


class Message(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, -300)

    def write_warning(self, text, sleep):
        self.write(text, align="center", font=("Courier", 12, "bold"))
        time.sleep(sleep)
        self.clear()
