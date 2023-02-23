
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


if __name__ == '__main__':
    while True:
        action = None
        user_choice = input('Do you want to (e)ncrypt or (d)ecrypt?\n')

        '''using lambda expression in order to be able to have the verification here instead of the end of questions'''
        if user_choice == 'e':
            action = lambda message, shift: print(caesar_encrypt(message, int(shift)))
        elif user_choice == 'd':
            action = lambda message, shift: print(caesar_decrypt(message, int(shift)))
        else:
            print('Please type either a or d; restarting')
            continue
        shift = input('Please enter the key (0 to 25) to use.\n')
        try:
            shift = int(shift)
            if 0 > shift > 25:
                print('Please input a number between 0 and 25; restarting')
                continue
        except:
            print('Please enter a number; restarting')
            continue
        message = input('Enter the message to encrypt.\n')
        if action:
            action(message, shift)


