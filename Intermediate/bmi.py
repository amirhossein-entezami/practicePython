# calculate your BMI
receive_weight = int(input("Please import your weight in kilograms: "))
receive_height = float(input("Please import your height in centimeter: "))

# out put should be round number -> we use int() function
bmi = int(receive_weight / (receive_height ** 2))

print(f"Your bmi is {bmi}")