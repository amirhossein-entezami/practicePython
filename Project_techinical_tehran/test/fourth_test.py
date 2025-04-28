# barnamei benvisid ke se ta add begire bege tashkil mosalas midan ya kheir

receive_user = input("enter 3 numbers: ").split()

x = int(receive_user[0])
y = int(receive_user[1])
z = int(receive_user[2])

if 10 < x < 60:
    if 10 < y < 60:
        if 10 < z < 60:
            print("yes make a triangle! ")
        else:
            print("no, do not make a triangle!")
    else:
        print("no, do not make a triangle!")
else:
    print("no, do not make a triangle!")
