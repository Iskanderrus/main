from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen settings:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Голодный червячок")
screen.tracer(0)

# Introducing main parts of the game:
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.board_refresh()

# Introducing controls:
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game cycle:
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with the food:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.board_refresh()

    # Detect collision with the wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
