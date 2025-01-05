# make rollercoaster and filter the age
# the rollercoaster big game in game city
print("welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("Your can ride the rollercoaster!")
    age = int(input("Please Enter your age in years? "))
    if age <= 18:
        print("You should pay $7.")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("You should pay $12.")
else:
    print("Your can't ride the rollercoaster!")