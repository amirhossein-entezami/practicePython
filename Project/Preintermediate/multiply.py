"""barnamei benevisid yek add va yek zarib daryaft kone va
amal zarb an add dar zaribesh ro 10 bar tekrar mikone"""

add = int(input("ye add delkhah vared konid: "))
zarib = int(input("ye add be onvan zarib addet vared kon: "))
num = 0
for i in range(10):
    add *= zarib
    num += 1
    print(f"dafee {num}: ", add)
