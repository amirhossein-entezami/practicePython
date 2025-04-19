""" barnamei ke ta vaghti ke karbar 0 nadadeh add bgire dar nahayat
majome tedad miangin max va min ro elam kone"""

receive_user = int(input("please enter a number: "))
receive_user_2 = int(input("please enter another number: "))

add = receive_user_2
sum = 0
while receive_user != 0:
    add += 1
    sum = receive_user
    majme = receive_user + sum
    for i in range(1, receive_user):
        pass
    print(f"tedad-> {i}")
    avg = sum + receive_user / 2
    if receive_user > add:
        print(f"max-> {receive_user}")
    elif receive_user < add:
        print(f"min-> {receive_user}")
    print(f"majmoe-> {majme}")
    receive_user = int(input("please enter a number: "))
