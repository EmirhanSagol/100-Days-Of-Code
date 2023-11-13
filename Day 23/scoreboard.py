from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 50, "normal"))

    def show_level(self):
        self.goto(-225, 250)
        self.write(arg=f"LEVEL: {self.level}", move=False, align="center", font=("Arial", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.show_level()