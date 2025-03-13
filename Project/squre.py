""" barnamei ke 2 add daryaft kone bege tashkil moraba midahand ya na? """
print("2 add vared konid!")
num_1 = int(input("add aval: "))
num_2 = int(input("add dovom: "))

if num_1 == num_2:
    moraba = (num_2 + num_1 / 2) ** 2 - num_1 ** 2 / 4 
    print("moraba tashkil mishavad!")
else:
    print("moraba nist!")
