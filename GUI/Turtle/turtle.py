# Import Library
# import turtle
from Turtle import Turtle, Screen
import random

# Start the project with Turtle
timmy = Turtle()

# Choose The shape of Turtle
timmy.shape("turtle")

# Choose Color
timmy.color("red")

# Square Shape -> long way
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# Square Shape -> short way
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Tutle go forward with Dash way
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# TODO- Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon

# This is pentagon
num_sides = 5
for _ in range(num_sides):
    angle = 360 / num_sides
    timmy.forward(100)
    timmy.right(angle)

# This is full package with color
colors = ['CornFlowerBlue', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'LightSalmon']

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)


for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    # draw_shape(shape_side_n)

# Draw a Random Walk

colors = ['CornFlowerBlue', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'LightSalmon']
direction = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fast")

timmy.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomm_color = (r, g, b)
    return randomm_color

directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")

# end of the project
screen = Screen()
screen.exitonclick()
