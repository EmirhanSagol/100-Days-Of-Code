from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed(0)
        self.seth(90)
        self.start_pos()

    def move(self):
        self.forward(10)

    def start_pos(self):
        self.goto(0, -275)
