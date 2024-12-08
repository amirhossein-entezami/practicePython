# calculate your age in day, month and year
print("Welcome to caculator age to month and year!!!")
receive_user = int(input("Enter your age= "))
remaining_age = 90 - receive_user
day = remaining_age * 365
week = remaining_age * 52
month = remaining_age * 12

print(f"Your age left in day is: {day} and in week is {week} and in month is {month}")