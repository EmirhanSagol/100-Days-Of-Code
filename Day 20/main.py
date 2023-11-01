from turtle import Turtle, Screen
from snake import Snake
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()

screen.tracer(0)
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
