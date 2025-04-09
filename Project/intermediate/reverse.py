""" barnamei benvisid ke ta zamani ke user add 10 nanade az karbar add begire
va barresi kone on add ba maghlobesh barabare ya na ex. 522 -> 225 (*) - 303 -> 303 (+) """

receive_user = input("please enter a number: ")

if int(receive_user) == 10:
    print("End!")
else:
    reverse_user = receive_user[::-1]
    print(f"your input number is -> {receive_user}")
    print(f"Reverse your input is -> {reverse_user}")
    if int(receive_user) == int(reverse_user):
        print("your final result is -> **yes!**")
    else:
        print("your final result is -> --no!--")
