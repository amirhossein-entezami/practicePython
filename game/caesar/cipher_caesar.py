from art_caesar import logo
print(logo)

# alphabet for encode and decode letter user
alphabet = ['a', 'b', 'c', 'd', 'e', 'f'
    , 'g', 'h', 'i', 'j', 'k', 'l'
    , 'd', 'm', 'n', 'o', 'p', 'q'
    , 'r', 's', 't', 'u', 'v', 'w'
    , 'x', 'y', 'z', 'a', 'b', 'c'
    , 'd', 'e', 'f', 'g', 'h', 'i'
    , 'j', 'k', 'l', 'd', 'm', 'n'
    , 'o', 'p', 'q', 'r', 's', 't'
    , 'u', 'v', 'w', 'x', 'y', 'z']

# Give input user for start the program
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))
