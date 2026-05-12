from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(user_choice, user_text, shift_number):
    final_text = ""
    for letter in user_text:
        if letter not in alphabet:
            final_text += letter
        else:
            if user_choice == "decode":
                back_position = alphabet.index(letter) - shift_number
                final_text += alphabet[back_position]
            else:
                position= alphabet.index(letter)- len(alphabet)
                shifted_position= position+shift_number
                final_text += alphabet[shifted_position]
    print(f"Here is the {user_choice}d result: {final_text}")


caesar_cipher_on = True

while caesar_cipher_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

    restart = input("Would you like to continue? yes/no: \n").lower()
    if restart == "no":
        caesar_cipher_on = False
        print("Bye! Have a nice day!")
