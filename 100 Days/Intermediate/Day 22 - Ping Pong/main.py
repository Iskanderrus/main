from turtle import Screen
from paddle import Paddle
import time

# Screen settings:
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Пинг-Понг")
screen.tracer(0)

# Introducing main parts of the game:
left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))

# Introducing controls:
screen.listen()
screen.onkey(left_paddle.up, "a")
screen.onkey(left_paddle.down, "z")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

# Main game cycle:
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.00001)
#
#     # Detect collision with the food:
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend_snake()
#         scoreboard.board_refresh()
#
#     # Detect collision with the wall:
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()
#
#     # Detect collision with own tail:
#     for segment in snake.segments[1:]:
#         if snake.head.distance(segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()

screen.exitonclick()
