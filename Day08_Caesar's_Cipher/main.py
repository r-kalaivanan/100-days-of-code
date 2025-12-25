alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    encrypted_text = ""
    for letter in text:
        encrypted_text += alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
    return encrypted_text

def decrypt(text,shift):
    decrypted_text = ""
    for letter in text:
        decrypted_text += alphabet[(alphabet.index(letter) - shift) % len(alphabet)]
    return decrypted_text

cipher = True
while cipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))

    if direction == "encode":
        print("The encrypted message : ",encrypt(text_input,shift_input))
    elif direction == "decode":
        print("The decrypted message : ",decrypt(text_input,shift_input))
    else:
        print("Invalid Input!")

    choice = input("Do you wanna go again ? [y/n] : ")
    if choice == 'n':
        cipher = False

print("Thanks!")


