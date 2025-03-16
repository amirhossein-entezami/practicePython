""" Barnamei ke gheymat mashion migire age balaye 400t
bod 20% malyat pash bezane dar gheyr in sorat 10% malyat bezane! """
receive_user = int(input("Lotfan mablagh morede nazar khod baraye khodro mord nazr benevisid(ex. 300): "))
if receive_user <= 400:
    expensive = round(receive_user * 0.2)
    print(f"Ba ehtesab 20% maliat -> ({expensive}t) bayad bishtar pardakht shavad")
    print(f"Dar kole bayad -> ({receive_user + expensive}t) pardakht shavad")
else:
    cheap = round(receive_user * 0.1)
    print(f"Ba ehtesab 10% maliat -> ({cheap}t) bayad bishtar pardakht shavad")
    print(f"Dar kole bayad -> ({receive_user + cheap}t) pardakht shavad")
