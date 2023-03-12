def caesar_encrypt(text: str, shift: int) -> str:
    '''i transform the string into a list of characters with [*text], then for every character in there
    i get its numerical value with ord(), i add the shift to it and use module to normalize it,
     i turn it back into a character with chr(), and then i concatenate them back
    into a string with ''.join()'''
    return 'Shift out of bounds' if (shift < 0 or shift > 25) else\
        ''.join([chr((ord(char) + shift) % 90 + ((ord(char) + shift) > 90 and 64)) if 65 <= ord(char) <= 90 else char
                 for char in [*text.upper()]])


def caesar_decrypt(text: str, shift: int) -> str:
    ''' same thing, but using an if instead of the and expression
    the could habve been easier to understand, but i wanted to have everything in the return statement, as a challenge.
    '''
    return 'Shift out of bounds' if (shift < 0 or shift > 25) else \
        ''.join([chr(90 - 64 % (ord(char) - shift) if ord(char) - shift < 65 else ord(char) - shift) if 65 <= ord(char) <= 90 else char
                 for char in [*text.upper()]])


def caesar_breaker(text):
    for i in range(26):
        print('\n', caesar_decrypt(text, i))


if __name__ == '__main__':
    encryptedMessage = caesar_encrypt('This is a message for testing the caesar encryption', 5)
    print(encryptedMessage)
    caesar_breaker(encryptedMessage)

