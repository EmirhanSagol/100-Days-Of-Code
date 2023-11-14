from turtle import Turtle

FONT_SIZE = 20


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(x=0, y=270)
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", move=False,
                   align="center", font=("Courier", FONT_SIZE, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()
