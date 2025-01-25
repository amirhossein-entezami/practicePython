# In this project we work with oop -> object-oriented-programming 
# Library
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")

#( Object )( attributes )
#    |           |
# car.speed

my_screen = Screen()
print(my_screen.canvheight)

#( Object )( methods )
#    |         |
# car.stop()

timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Chamander", "Pangoro"])
table.add_column("Type", ["Electric", "Water", "water"])

print(table)