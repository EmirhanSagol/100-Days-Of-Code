from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_scoreboard = Scoreboard(50)
l_scoreboard = Scoreboard(-50)

screen.listen()
screen.onkeypress(fun=r_paddle.move_up, key="w")
screen.onkeypress(fun=r_paddle.move_down, key="s")

screen.onkeypress(fun=l_paddle.move_up, key="Up")
screen.onkeypress(fun=l_paddle.move_down, key="Down")


while True:
    time.sleep(ball.move_speed)
    ball.move()

    #  Detect Wall Bounce
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bouncing_wall()

    #  Detect Paddle Bounce
    if ((ball.distance(l_paddle) < 60 and ball.xcor() <= -330) or
            (ball.distance(r_paddle) < 60 and ball.xcor() >= 330)):
        ball.bouncing_paddle()

    #  Detect Score
    if ball.xcor() > 400:
        r_scoreboard.increase_score()
        ball.start()
        time.sleep(3)
    elif ball.xcor() < -400:
        l_scoreboard.increase_score()
        ball.start()
        time.sleep(3)

    screen.update()

screen.exitonclick()
