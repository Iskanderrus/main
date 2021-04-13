alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(start_text, shift_amount, cipher_direction):
    encoded = ''
    for char in start_text:
        if char not in alphabet:
            encoded += char
        elif cipher_direction == "encode":
            if (alphabet.index(char) + shift_amount) >= 26:
                encoded += alphabet[(alphabet.index(char) + shift_amount) % 26]
            else:
                encoded += alphabet[alphabet.index(char) + shift_amount]
        elif cipher_direction == "decode":
            if (alphabet.index(char) - shift_amount) < 0:
                encoded += alphabet[(alphabet.index(char) - shift_amount) % 26]
            else:
                encoded += alphabet[alphabet.index(char) - shift_amount]
    print(f'The {cipher_direction}d text is {encoded}')


question = True
while question:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
    question = input("Do you want to continue? y / n: \n")
    if question == 'n':
        question = False
        print('Ave, Caesar, morituri te salutant!')

