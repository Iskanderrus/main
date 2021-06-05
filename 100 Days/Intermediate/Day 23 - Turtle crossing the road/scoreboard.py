from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.speed = 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-230, 230)
        self.write(f"Уровень: {self.score}\nСкорость: {self.speed}", align="Left", font=("Courier", 12, "bold"))

    def add_point(self):
        self.score += 1
        self.speed += 1
        self.refresh()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Черепашку переехали на уровне {self.score}\nпри скорости "
                   f"{self.speed}", align="Center", font=("Courier", 18, "bold"))
