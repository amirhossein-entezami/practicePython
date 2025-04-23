""" barnamei benvisid 10 add begire bege max kodome """
print("10 add delkhah vared konid, ta maximum behet bedam!")

add = 1
max = 0
for i in range(10):
    num = int(input(f"number {add}: "))
    add += 1
    if num > max:
        max = num
print(f"maximum -> {max}")
