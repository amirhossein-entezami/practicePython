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

