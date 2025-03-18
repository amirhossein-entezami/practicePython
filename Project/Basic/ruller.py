"""barname ke milimter dryaft mikone va 
mige chand santi meter va chand meter hast"""

receive_num = int(input("add bede begam chand centimetere ? va chand meter?(!!faghat 4 ragham!!): "))

if 999 < receive_num < 10000:
    meter = receive_num // 1000
    centimeter = receive_num // 10
    print(f"addi ke be onvan milimeter vared cardi: {receive_num}")
    print(f"meter -> {( meter )} meter")
    print(f"centimeter -> {( centimeter )} centimeter")
else:
    print("4 raghami khastam na kamtar na bishtar!")
