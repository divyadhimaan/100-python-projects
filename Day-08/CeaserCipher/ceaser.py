from ceaser_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(input_text, shift_number, direction):
    transformed_text = ""
    if direction == "decode":
        shift_number *= -1
    for letter in input_text:
        if letter in alphabet: 
            new_index = (alphabet.index(letter) + shift_number) % 26 
            transformed_text += alphabet[new_index]
        else:
            transformed_text += letter

    print(f"The {direction}d text: {transformed_text}")

is_continue = True
while is_continue:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(input_text=text, shift_number=shift, direction=direction)

    want_to_continue = input("Do you want to continue? Type 'yes' or 'no'.\n")
    is_continue = False if want_to_continue == "no" else True
