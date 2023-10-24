import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

Turtles = []
Colors = ["red", "yellow", "green", "purple", "blue", "orange"]

for _ in range(6):
    t = Turtle("turtle")
    Turtles.append(t)

for i, t in enumerate(Turtles):
    t.color(Colors[i])
    t.speed(1)
    t.penup(),
    t.goto(-230, i * 30 - 75)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in Turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print("Your turtle won the race. Congratulation!")
            else:
                print(f"Your turtle lose the race. Winner is {winning_color}")

        random_distance = random.randint(0, 10)
        t.forward(random_distance)


screen.exitonclick()
