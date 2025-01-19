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


######################################

# Reproduce the Bug
# False -------------------
from random import randint
dice_imgs = ["test_1","test_2","test_3","test_4","test_5","test_6",]
dice_num = randint(1,6)
print(dice_imgs[dice_num])

# True----------------------
from random import randint
dice_imgs = ["test_1","test_2","test_3","test_4","test_5","test_6",]
dice_num = randint(0,5)
print(dice_imgs[dice_num])

# Play Computer

# False--------------------
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# True----------------------------
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

########################################

# Fix the Errors
# # False-------------------------
# age = input("How old are you? ")
# if age > 18:
# print("you can drive at age {age}.")

# True--------------------------
age = int(input("How old are you? "))
if age > 18:
    print(f"you can drive at age {age}.")


##########################################################

# Print is Your Friend
# False------------------------------
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words == pages * word_per_page
# print(total_words)

# True-------------------------------
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#########################################################

# Use Debugger
# False------------------
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)

# mutate([1,2,3,5,8,13])


# True--------------
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
# mutate([1,2,3,5,8,13])

############################################
# More practice
# False-------------
# number = int(input("Which number do you want to check? "))

# if number % 2 = 0:
#     print("The number is an even number.")
# else:
#     print("The number is an odd number.")

# True-------------
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("The number is an even number.")
else:
    print("The number is an odd number.")
