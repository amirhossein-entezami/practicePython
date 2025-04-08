""" fibonanchi """
num_1 = 1
num_2 = 1
num_3 = 0
my_counter = 0
counter = int(input("addad vared konid: "))
while my_counter <= counter:
    print(f"{num_3}")
    num_1, num_2 = num_2, num_3
    # num_2 = num_3
    num_3 = num_1 + num_2
    my_counter += 1
