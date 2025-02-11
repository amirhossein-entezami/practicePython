# Password Generator Project
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["_", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Weclome to the PyPassword Generator! ")

receive_letters = int(input("How many letter would you like in your password?\n"))
receive_symbols = int(input("How many symbols would you like?\n"))
receive_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level

password = ""

for char in range(1, receive_letters + 1):
    password += random.choice(letters)

for char in range(1, receive_symbols + 1):
    password += random.choice(symbols)

for char in range(1, receive_numbers + 1):
    password += random.choice(numbers)

print(f"Your new password in 'Eazy Level' is=> {password}")

# Hard Level
password_list = []

for char in range(1, receive_letters+ 1):
    password_list.append(random.choice(letters))

for char in range(1, receive_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, receive_numbers + 1):
    password_list.append(random.choice(numbers))

# This is extra for learning
print(password_list)
random.shuffle(password_list)
print(password_list)

# -------------------------

password = ""
for char in password_list:
    password += char

print(f"Your new password in 'Hard Level' is=> {password}")

# check