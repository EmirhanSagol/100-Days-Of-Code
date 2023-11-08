from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed(0)
        self.penup()
        self.goto(position)
        self.score = 0

    def move_up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
