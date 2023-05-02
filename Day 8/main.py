import art
print(art.logo)
end = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
punctuation = [" ", "!", "'", "+", "%", "&", "/", "(", ")", "=", "*", "?", "-", "_", "|", "}", "]", "[", "{", "½", "$", "#", "£", ">", "<", ",", ".", ";", ":"]

def ceaser_cipher(direction, shift, text):
    new_text = ""
    for letter in text:
        if letter in punctuation:
            new_text += letter
        else:
            if direction == "encode":
                letter_index = alphabet.index(letter) + shift
                if letter_index > 25:
                    letter_index = (letter_index % 25) - 1
            elif direction == "decode":
                letter_index = alphabet.index(letter) - shift
                if letter_index < 0:
                    letter_index += 26
            new_text += alphabet[letter_index]
    return new_text

while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    print(ceaser_cipher(direction, shift, text))

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n") 
    if restart == "no":
        end = True
        print("Goodbye!")

      
