# barnamei ke tabe ghadr motlagh anjam mideh

receive_user = int(input("Enter number: "))

# first way is->
# abs_receive_user = abs(receive_user)
# print(f"ghadr motlagh addet-> {abs_receive_user}")


# second way is ->
if receive_user > 0:
    print(f"ghadr motlagh addet-> {receive_user}")
elif receive_user < 0:
    print(f"ghadr motlagh addet-> {receive_user * -1}")
elif receive_user == 0:
    print(f"sefr mosbate dar natije khodeshe-> {receive_user}")
