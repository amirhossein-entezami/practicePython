""" barnamei ke ta zamani ke add zoj vared nakardim vorodi horof daryaft mikone 
va barrresi mikone palinrom barabare ya na!"""

recevie_char = input("please eneter name: ")
if int(recevie_char) % 2 == 0:
    print("this is integer az even!")
else:
    while True:
        recevie_char_inverse = recevie_char[::-1]
        if recevie_char == recevie_char_inverse:
            print("Yes this name is inverse!")
            print(f"inverse: {recevie_char_inverse}")
        else:
            print("No it's not inverse")
            print(f"inverse: {recevie_char_inverse}")
        recevie_char = input("please eneter name: ")
        
        # check