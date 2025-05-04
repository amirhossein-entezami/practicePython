# barnamei benevisid ke 3 ta add begire avg ro bede behomon

receive_user = input("3 ta add bede (ba fasele benvis) ta avg ro bedam: ").split()

x = int(receive_user[0])
y = int(receive_user[1])
z = int(receive_user[2])
count = 0
for i in receive_user:
    count += 1

avg = (x + y + z) / count
print(f"avarage: {avg}")

