alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
Text = input("Type your message:\n").lower()
Shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter not in alphabet:
            cipher_text += letter
            continue
        shifted_index = alphabet.index(letter) + shift_amount
        shifted_index = shifted_index % len(alphabet)
        cipher_text += alphabet[shifted_index]
    print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    output_text = ""
    for letter in plain_text:
        if letter not in alphabet:
            output_text += letter
            continue
        shifted_index = alphabet.index(letter) - shift_amount
        shifted_index = shifted_index % len(alphabet)
        output_text += alphabet[shifted_index]
    print(f"The encoded text is {output_text}")

if Direction == "encode":
    encrypt(plain_text=Text, shift_amount=Shift)
elif Direction == "decode":
    decrypt(plain_text=Text, shift_amount=Shift)