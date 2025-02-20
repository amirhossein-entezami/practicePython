# Import Library
# import turtle
from Turtle import Turtle, Screen

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

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

# end of the project
screen = Screen()
screen.exitonclick()
