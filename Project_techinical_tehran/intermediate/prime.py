""" barnamei ke yek add mikhone mige avale ya na  """

receive_user = int(input("please enter a number: "))

counter = 0
for aval in range(1, receive_user+1):
    if receive_user % aval == 0:
        counter += 1
if counter == 2:
    print("bale add avale!")
else:
    print("kheyr add aval nist!")
