from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.score = 0
        self.goto(x_cor, 200)
        self.show_score()

    def show_score(self):
        self.write(arg=self.score, move=False, align="center", font=("Arial", 66, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()