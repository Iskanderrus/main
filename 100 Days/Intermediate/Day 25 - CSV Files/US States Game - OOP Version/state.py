from turtle import Turtle


class StateUS(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def add_state(self, name, x_coord, y_coord):
        self.goto(x_coord, y_coord)
        self.write(name.title(), align="center", font=("Courier", 7, "bold"))
