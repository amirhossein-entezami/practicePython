""" barnamei benevisid ke yek matn ra be onvan ramz daryaft kone m an ra be ramz sezar tabdil konad"""

receive_user = input("please enter a word:")

list = ""
for sezar in receive_user:
    tak = chr(ord(sezar) + 3)
    list += tak
print(list)
