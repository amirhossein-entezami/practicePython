""" barname benvisid ke 5 ta add begire bege zoje ya farde """
print("5 bar add vared konid! ke bebinim zoje ya fard!")

add = 1
for count in range(5):
    num = int(input(f"number {add}: "))
    add += 1
    if num % 2 == 0:
        print(f"{num} is -> even")
    else:
        print(f"{num} is -> odd")

