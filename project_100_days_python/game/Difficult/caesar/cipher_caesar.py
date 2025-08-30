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


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is: {cipher_text}")

# Give input user for start the program
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    pass

# test 8 7 6 5 4 3