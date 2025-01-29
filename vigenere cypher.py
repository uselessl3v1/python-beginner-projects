
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset *direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message
#From this point is fully my own code
def encr_input():
    encryption_decryption = input("Encrypt or Decrypt? ").lower()

    if encryption_decryption == 'encrypt':
        encr_message = input('What is the message you want to encrypt? ')
        encr_key = input('What key do you want to use? ')
        final_encr = vigenere(encr_message, encr_key)
        print(f'Message: {encr_message}' )
        print(f'Encrypted message: {final_encr}')

    elif encryption_decryption == 'decrypt':
        decr_message = input('What is the message you want to decrypt? ')
        decr_key = input('What key do you want to use? ')
        final_decr = vigenere(decr_message, decr_key, -1)
        print(f'Encrypted message: {decr_message}')
        print(f'Decrypted message: {final_decr}')

    else:
        print("Please enter either encrypt or decrypt")
        encr_input()

encr_input()








