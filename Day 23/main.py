from turtle import Screen
from myturtle import MyTurtle
from car import Car
from scoreboard import Scoreboard
import random
import time


screen = Screen()
screen.setup(600, 600)
screen.title("Crossing Game")
screen.listen()

car = Car()
myTurtle = MyTurtle()
scoreboard = Scoreboard()

screen.onkeypress(fun=myTurtle.move, key="Up")

game_is_on = True
game_speed = 0.1
change_of_cars = 5

screen.delay(0)
scoreboard.show_level()


while game_is_on:
    time.sleep(game_speed)

    #  Creates car when game start
    if len(car.cars) < 12 * scoreboard.level:
        for i in range(0, 12 * scoreboard.level):
            car.game_start()

    #  Create Cars randomly
    if random.randint(0, 10) < change_of_cars:
        y_pos = random.randrange(-220, 250, 5)
        car.create_car(x_pos=290, y_pos=y_pos)
    car.move()

    #  Detect Crash
    for i in car.cars:
        if myTurtle.distance(i) < 23:
            scoreboard.game_over()
            game_is_on = False

    #  Detect Finishline
    if myTurtle.ycor() > 270:
        time.sleep(2)
        for i in car.cars:
            i.hideturtle()
        car.cars = []
        scoreboard.increase_level()
        myTurtle.start_pos()
        car.speed += -5
        change_of_cars += 1

    car.remove_car()

screen.exitonclick()
