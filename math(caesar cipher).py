a = 8 % 3
print(a)


def caesar_cipher(text, key):
    output = ""
    for i in range(len(text)):
        character = text[i]
        location = alphabets.find(character)
        new_location = location + int(key) % 26
        # print(character, location, new_location)
        output += alphabets[new_location]
    print(output)


alphabets = "abcdefghijklmnopqrstuvwxyz"
print(len(alphabets))

text_input = input("Enter text: ")
key_input = input("Enter a number: ")
caesar_cipher(text_input, key_input)
print()


def caesar_decrypt(text, key):
    output = ""
    for i in range(len(text)):
        character = text[i]
        location = alphabets.find(character)
        new_location = location - int(key)
        # print(character, location, new_location)
        output += alphabets[new_location]
    print(output)


decrypt_text_input = input("Enter text: ")
decrypt_key_input = input("Enter a number: ")
caesar_decrypt(decrypt_text_input, decrypt_key_input)
print()
