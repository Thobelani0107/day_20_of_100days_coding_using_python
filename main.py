from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake


import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
score=Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) <15:
        food.food()
        snake.extend()
        score.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.Wall_collition()
        game_is_on=False
        score.Wall_collition()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on=False
            score.Wall_collition()






screen.exitonclick()
