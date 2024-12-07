print('''                         _._
                               .-~ | ~-.
                               |   |   |
                               |  _:_  |                  .---:~-----:
                             .-"~~ | ~~"-.                |   |      |
            _.-~:.           |     |     |                |   |      |
           |    | `.         |     |     |                |   |      |
  _..--~:-.|    |  |         |     |     |                |   |      |
 |      |  ~.   |  |         |  __.:.__  |                |   |      |
 |      |   |   |  |       .-"~~   |   ~~"-.              |   |      |
 |      |   |  _|.--~:-.   |       |       |         .:~-.|   |      |
 |      A   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
 |      M   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      I   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      R   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
print("Welcome to the secret of this city!!!")
print("Your mission is to find the treasure.")
street = input("You're at a cross street. Where do you want to go? 'left' or 'right' ").lower()
if street == 'right':
    print('You are game over!')
elif street == 'left':
    bank = input("You come to the bank, There is an a shelf in the middle of the bank. What is your reaction? 'bring' or 'wait' ").lower()
    if bank == 'bring':
        print('You are game over!')
    elif bank == 'wait':
        strongbox = input("You arrive at the strongbox of bank. There are 3 doors. choose a one of them. Which color do you choose? 'red' or 'yellow' or 'blue' ").lower()
        if strongbox == 'yellow':
            print('You are Win!!')
        else:
            print('You are game over!')
