# Guess word
# My Turn
import random

numbers = []
for i in range(101):
    add_number = numbers.append(i)

random_number = random.choice(numbers)

should_continue = True
while should_continue:
    def mode(easy, hard, difficulty):
        def guess(user_number, computer_number):
            global should_continue
            if user_number > computer_number:
                print("Your number is too high")
            elif user_number < computer_number:
                print("Your number is too low")
            elif user_number == computer_number:
                print(f"Correct, computer number is {computer_number}, Your number is {user_number}")
                should_continue = False
            else:
                print("wrong")

        guess(user_number=receive_user, computer_number=random_number)


    receive_user = int(input("please enter number: "))
    receive_mode = input("please enter mode, easy - hard - difficulty: ")

# work and new file after
