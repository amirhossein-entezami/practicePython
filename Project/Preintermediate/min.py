""" barnamei benvisid 10 add begire bege min kodome """

print("10 add delkhah vared konid, ta minimum behet bedam!")

add = 2
recive_min = int(input("number 1: "))
min = recive_min
for i in range(9):
    num = int(input(f"number {add}: "))
    add += 1
    if num < min:
        min = num
print(f"minimum is - > {min}")
