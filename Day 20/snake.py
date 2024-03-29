from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in range(3):
            snake_piece = Turtle("square")
            snake_piece.color("white")
            snake_piece.penup()
            snake_piece.goto(-i * 20, 0)
            self.segment.append(snake_piece)

    def move(self):
        for segment in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[segment - 1].xcor()
            new_y = self.segment[segment - 1].ycor()
            self.segment[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
