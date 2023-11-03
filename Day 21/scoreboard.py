from turtle import Turtle

FONT_SIZE = 20


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(x=0, y=270)
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Courier", FONT_SIZE, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER.", move=False, align="center", font=("Courier", 30, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()
