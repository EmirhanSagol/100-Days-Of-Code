from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.states = []
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.score = 0

    def create_state(self, state_name, x_cor, y_cor):
        self.goto(x_cor, y_cor)
        self.states.append(state_name)
        self.write(arg=state_name, move=True, align="center", font=("Arial", 10, "normal"))

    def wrong_answer(self):
        self.goto(0, -200)
        self.write(arg=f"Your answer is wrong. Game Over.\n"
                       f"Score: {self.score}", align="center", move=False, font=("Arial", 24, "bold"))

    def increase_score(self):
        self.score += 1