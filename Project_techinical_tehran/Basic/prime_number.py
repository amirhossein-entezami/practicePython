""" barnamei ke yek add 3 raghami migire ye add tak ragahmi ham migire be
onvan meyar baraye sefr kardan khane (n) add aval """

receive_user = int(input("lotfan add 3 raghami vared konid!: "))
compare = input("meyar addad bede ke on addo be tartib az chp be rast 0 koanm! 1 - 3: ")

if compare == "1":
    sadgan = str((receive_user // 100 * 0)) + str(receive_user % 100)
    print(sadgan)
elif compare == "2":
    dahgan = ((receive_user % 100) // 10 ) * 10 - receive_user
    print(abs(dahgan))
elif compare == "3":
    yekan = (receive_user % 10) - receive_user
    print(abs(yekan))