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
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

# end of the project
screen = Screen()
screen.exitonclick()
