from turtle import Turtle
import random

COLORS = ["forest green", "dark green", "red", "gold", "dark cyan", "medium blue", "gray",
          "black", "deep pink", "purple", "orange", "saddle brown", "indigo"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.speed = -10
        #  self.create_car()
        #  self.start_pos(self.cars[-1])

    def create_car(self, x_pos, y_pos):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.speed(0)
        self.cars.append(car)
        self.start_pos(self.cars[-1], x_pos, y_pos)

    def game_start(self):
        new_x = random.randrange(-250, 250, 5)
        new_y = random.randrange(-250, 250, 5)
        self.create_car(new_x, new_y)

    def start_pos(self, car, x_pos, y_pos):
        car.goto(x=x_pos, y=y_pos)

    def move(self):
        for i in range(0, len(self.cars)):
            new_x = self.cars[i].xcor()
            new_y = self.cars[i].ycor()
            self.cars[i].goto(new_x + self.speed, new_y)

    def remove_car(self):
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)
