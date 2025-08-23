standard_list = []

while True:
    print("\n👍->  please choose")
    print("1) Add Student") # record yek danesh amoz ro daryaft kone va zakhire kone!
    print("2) Delete Student") # namayesh tamam danesh amoz ha va entekhab baraye hazf!
    print("3) Replace Student") # kolesh namayesh dade beshe - yek record entekhab bashe va maghadir jadid beshe midim!
    print("4) Show Information") # neshon dadan etelwat - miad behet shomare desnshjo mide!    
    print("5) Find Student") # neshon dadan etelwat - miad behet shomare desnshjo mide!
    print("6) Exit\n") # khoroj az barnameh
    # this is input for 
    press = input("kodom option?(add vared konid): ")
    if press == "1":
        print("shoma vared option 1 shodid bayad inja etleaat jadid vared konid!!!")
        tedad_user = 0
        tedad_daneshjo = int(input("chndta danshjo mikhay info bedi?(add bede): "))
        for shomaresh_danshjo in range(tedad_daneshjo):
            tedad_user += 1
            print(f"user shomare -> {tedad_user}")
            for j in range(1):
                madarek = []
                s_daneshjo = input("Shomare Daneshjo: ")  
                if len(s_daneshjo) < 9 :
                    print("Warning!")
                    print("shomare danshjo bayad 9 raghami bashad!")
                    s_daneshjo = 0
                    s_daneshjo = input("Shomare Daneshjo: ")
                    if len(s_daneshjo) < 9:
                        print("Erorr!")
                        print("-> barname baste shod dobare az aval!!")
                        break
                if len(s_daneshjo) > 9:
                    print("tedad shomrare daneshjo bayad kamater az 10 ta bashad!!!!!")
                    break
                name = input("Esmet Ro Bede: ")
                family = input("Familit ro bede: ")
                age = int(input("Sen Ro bede:"))
                if age < 7:
                    print("senet kame!!!")
                    break
                if 7 <= age < 80:
                    print("senet okeye!")
                if 80 <= age < 100:
                    print("senet zyade!")
                    break
                if age >= 100:
                    print("mordi ke!!!!!")
                    break
                sum = 0
                tedad_madrak = int(input("Tedad madrakat chndtas?(add bede): "))
                for i in range(tedad_madrak):
                    sum += 1
                    madrak = input(f"madrak shomare -> {sum} ro bede: ")
                    if madrak == "":
                        print("nemitoni madrak khali bazari!!!")
                        madrak = input(f"madrak shomare -> {sum} ro bede: ")
                        if madrak == "":
                            print("barname be moshkel khord dobare az aval bezan!!")
                            break
                    madarek.append(madrak)
                dars = input("Dars Ro Bede: ")
            std = [s_daneshjo, [name, age, [madarek], dars]]
            standard_list.append(std)
            print(f"info persons-> {standard_list}")
    elif press == "2":
        print("inja shoma eteleat ro pak mikonid!!!")
        standard_list.remove(std)
        print(standard_list)
    elif press == "3":
        print("dar in ghesmat shoma ghesmat mored nazar ro taghir midid!!!")
        print(standard_list)
        last = input("chio mikhay hazf koni?: ")
        new = input("chio mikhay add koni?: ")
        standard_list.index(last, new)
    elif press == "4":
        print(f"{standard_list}\n")
    elif press == "5":
        find_element = input("jostojo kalame ke mikhay?: ")
        standard_list.find(find_element)
    elif press == "6":
        print("Exit!!!")
        break 
# checked this file for 8