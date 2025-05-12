from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# start of the program
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# variable for turtle
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# end of the program
screen.exitonclick()
