"""barnamei ke factorial add ro namayesh bede"""

receive_user = int(input("please enter a number: "))

factorail = 1
for i in range(1, receive_user+1):
    factorail = factorail * i
print(f"the factorial of {receive_user} is {factorail}")
