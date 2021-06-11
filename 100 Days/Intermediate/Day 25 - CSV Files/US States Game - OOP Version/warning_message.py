from turtle import Turtle
import time


class Message(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 0)

    def add_warning(self, text):
        self.write(text, align="center", font=("Courier", 12, "bold"))
        time.sleep(1.5)
        self.clear()
