"""barnamei benevisid ke 4 ta add migire va mige
add kamele ya na age kamel bod payam bede perfect"""

number = int(input("ye add vared kon ke begam kamele ya na! : "))

sum = 0
for i in range(1, number):
    if number % i == 0:
        sum += i
if sum == number:
    print("perfect!")
else:
    print("perfect nist!")

