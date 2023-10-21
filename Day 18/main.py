from turtle import Turtle, Screen
import random
import colorgram


"""
pallete = []
colors = colorgram.extract('image.jpg', 40)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    pallete.append(new_color)

print(pallete)
"""

my_turtle = Turtle()
screen = Screen()
my_turtle.speed(0)
my_turtle.penup()

x_starting_pos = -500
y_starting_pos = -420

my_turtle.sety(y_starting_pos)
color_list = [(0.831, 0.584, 0.373), (0.843, 0.314, 0.243), (0.184, 0.369, 0.557), (0.906, 0.855, 0.361),
              (0.58, 0.259, 0.357), (0.086, 0.106, 0.157), (0.608, 0.286, 0.235), (0.478, 0.655, 0.765),
              (0.157, 0.086, 0.114), (0.153, 0.075, 0.059), (0.82, 0.275, 0.349), (0.753, 0.549, 0.624),
              (0.153, 0.514, 0.357), (0.49, 0.702, 0.553), (0.294, 0.643, 0.376), (0.898, 0.663, 0.718),
              (0.059, 0.122, 0.086), (0.2, 0.216, 0.4), (0.914, 0.863, 0.047), (0.624, 0.694, 0.212),
              (0.388, 0.173, 0.247), (0.137, 0.643, 0.769), (0.918, 0.671, 0.635), (0.412, 0.173, 0.153),
              (0.643, 0.82, 0.733), (0.592, 0.808, 0.863), (0.38, 0.498, 0.659), (0.133, 0.318, 0.192),
              (0.706, 0.737, 0.824), (0.329, 0.255, 0.118), (0.063, 0.302, 0.416)]

for _ in range(20):
    my_turtle.goto(x_starting_pos, my_turtle.ycor() + 40)
    for i in range(19):
        my_turtle.forward(50)
        my_turtle.dot(25, random.choice(color_list))

screen.exitonclick()
