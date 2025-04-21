"""2- barnamei benevisid ke yek reshte varzeshi daryaft kone 
va tedad tekrar haye kalamat ra be hamrah khode an namayesh bede """

receive_user = input("please enter name of sport: ")

tedad = 0
ind_ = 0
repeat = ""
while ind_ < len(receive_user):
    shomrandeh = 0
    for num_reap in receive_user:
        if num_reap == receive_user[ind_]:
            shomrandeh += 1
    if receive_user[ind_] not in repeat:
        print(receive_user[ind_], "=", shomrandeh)
        repeat += receive_user[ind_]
    ind_ += 1
