# we create function and learn about it.
def greet():
    print("Hello")
    print("How are you?")
    print("What is your name?")


greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")


greet_with_name("Amir")

# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name} welcome to {location}")


greet_with("John", "florida")

