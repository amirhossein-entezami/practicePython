# make dibugging check file
# Describe Problem
# False -----------
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")
my_function()

# True ------------
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it!")
my_function()
