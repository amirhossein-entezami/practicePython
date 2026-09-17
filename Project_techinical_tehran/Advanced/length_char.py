""" barnamei ke yek reshte ra az vorodi be hamrah yek add khandeh, tamai kalamat reshte be tol an add namayesh midahad """

receive_user = input("please enter a country: ")
receive_tekrar = int(input("chnd bakhsh chnd bakkhsh shavad: "))

""" way 1 """
# ezafe = 0
# list = ""
# for joda in receive_user:
#     khoroji = receive_user[ezafe:receive_tekrar]
#     ezafe += 1
#     receive_tekrar += 1
    # print(khoroji)

""" way 2 """
final_word = ""
for i in range (len(receive_user)):
    harf = receive_user[i:receive_tekrar + i]
    if len(harf) < receive_tekrar:
        break
    else:
        # print(receive_user[i:receive_tekrar + i])
        final_word += harf + " "
print(final_word)