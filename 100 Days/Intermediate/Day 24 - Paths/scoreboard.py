from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")


def get_high_score(data):
    with open(data, mode="r") as file:
        high_score = file.read()
    return int(high_score.strip())


def write_high_score(data, score):
    with open(data, mode="w") as file:
        file.write(score)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.counter = -1
        self.penup()
        self.high_score = get_high_score("data.txt")
        self.color('white')
        self.hideturtle()
        self.goto(0, 260)

    def reset(self):
        if self.counter > int(self.high_score):
            self.high_score = self.counter
        write_high_score("data.txt", str(self.high_score))
        self.counter = -1
        self.board_refresh()

    def board_refresh(self):
        """
        Function to clean the scoreboard of the game and assign the new score.
        :return: None
        """
        self.clear()
        self.counter += 1
        self.write(f"Счёт: {self.counter}. Наивысший балл: {self.high_score}.", align=ALIGNMENT, font=FONT)
