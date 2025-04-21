""" 1- barnamei ke yek reshte ra khandeh va har kalame ra dar kenar code ascii an zakhire karde va darnayt
tamami an ra namayesh midahad va hamchenin migoyad kodamin kalame bozorgtrain code assci ra dashte"""

receive_user = input("plz enter word: ")

row = ""
max = ord(receive_user[0])
for repeat in receive_user:
    ord_ = ord(repeat)
    print(f"{repeat}  ->  {ord_}")
    if ord_ > max:
        chr_= chr(ord_)
        max = ord_
print(f"bishtarin meghdar kalame-> ( {chr_} ) ke ascci barabr -> ( {max} )")
