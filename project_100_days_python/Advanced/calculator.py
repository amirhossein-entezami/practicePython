# make a calculator
# This is my practice
# Calculator
def calculator(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    elif operator == '-':
        return num_2 - num_1
    elif operator == '*':
        return num_1 * num_2
    elif operator == '/':
        return num_1 / num_2
    else:
        print("this is wrong type!!!")

receive_num_1 = int(input("What's the first number? "))
print("""
+
-
*
/
""")
receive_operator = input("Pick an operation: ")
receive_num_2 = int(input("What's the second number? "))
calc = calculator(num_1=receive_num_1, num_2=receive_num_2, operator=receive_operator)
print(f"{float(receive_num_1)} {receive_operator} {float(receive_num_2)} = {float(calc)}")
# test 8 7