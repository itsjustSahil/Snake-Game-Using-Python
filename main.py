from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

# Create game screen and set up its properties
screen = Screen()
screen.setup(width =600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# snake movement logic
is_game_on = True
snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkeypress(lambda: snake.snake_control("w"), "w")
screen.onkeypress(lambda: snake.snake_control("s"), "s")
screen.onkeypress(lambda: snake.snake_control("a"), "a")
screen.onkeypress(lambda: snake.snake_control("d"), "d")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # Collision with food logic
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.snake_extend()

    # Collision with wall logic
    if snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 or snake.segment[0].ycor() > 290 or snake.segment[0].ycor() < -290:
        is_game_on = False
        score.game_over()

    # Collision with tail logic
    for body_part in snake.segment[1:]:
        if snake.segment[0].distance(body_part) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()
