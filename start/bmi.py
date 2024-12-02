# calculate your BMI
receive_weight = int(input("Please enter your weight in kilograms: "))
receive_height = float(input("Please enter your height in centimeter: "))

bmi = int(receive_weight / (receive_height ** 2))

print(f"Your bmi is {bmi}")