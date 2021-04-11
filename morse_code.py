import os
import sys

"""
    MORSE CODE ENCODER 
    AND DECODER
"""

MORSE_CODE = {
    "A": "-...", "B": ".-", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---",

    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
    "T": "-",

    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", ".": ".-.-.-", "0": "-----",
    "1": ".----",

    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "(": "-.--.",

    ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "#": ".-.-.", "-": "-....-", "_": "..--.-",

    '"': ".-..-.", "$": "...-..-", "@": ".--.-.", "?": "..--..", "!": "-.-.--"
}


# TO GET ONLY THE KEYS (LETTERS) FROM THE DICTIONARY
LETTERS = list(MORSE_CODE.keys())
# TO CONVERT THE KEYS INTO LOWER CASE, JUST IN CASE OF USER INPUT
LETTERS = [i.lower() for i in LETTERS]
# TO GET THE MORSE CODE VALUES FROM THE DICTIONARY
MORSE_VALUES = list(MORSE_CODE.values())

# FUNCTION TO GET USER INPUT


def get_input():
    while True:  # AN INFINITE LOOP FOR TAKING USER INPUT
        # GET MODE FROM USER
        mode = input('Would you like to encode (e) or decode (d): ')
        if mode == 'e':
            choice = input(
                'Would you like to read from a file (f) or the console (c)? ')
            if choice == 'c':
                message = input('What message would you like to encode: ')
                print(encode(message))
                choice = input(
                    'Would you like to encode/decode another message (y/n)? ')
                if choice == 'y':
                    continue
                elif choice == 'n':
                    sys.exit('Thank you for using the program, goodbye!')
                else:
                    print('Invalid choice!')

            elif choice == 'f':
                filename = input('Enter filename: ')
                if file_exists(filename):
                    content = read_lines(mode, filename)
                    print(content)
                else:
                    print("File does not exist, Try Again!")

            else:
                print("Invalid choice!")

        elif mode == 'd':
            choice = input(
                'Would you like to read from a file (f) or the console (c)? ')
            if choice == 'c':
                message = input('What message would you like to encode: ')
                print(decode(message))
                choice = input(
                    'Would you like to encode/decode another message (y/n)? ')
                if choice == 'y':
                    continue
                elif choice == 'n':
                    sys.exit('Thank you for using the program, goodbye!')
                else:
                    print('Invalid choice!')

            elif choice == 'f':
                filename = input('Enter filename: ')
                if file_exists(filename):
                    content = read_lines(mode, filename)
                    print(content)
                else:
                    print("File does not exist, Try Again!")

            else:
                print("Invalid choice!")

        else:
            print('Invalid mode!')
            continue


# FUNCTION TO ENCODE MESSAGE (USER INPUT)
def encode(message):
    cipher = ''
    message = message.upper()  # CONVERTING USER INPUT TO UPPERCASE
    message = list(message)  # SAVING EACH CHARACTER IN USER INPUT IN A LIST
    for i in message:
        # LOOP THROUGH USER INPUT, AND IF THERE IS NO SPACE BETWEEN LETTERS, ADD SPACES
        if i != ' ':
            cipher = cipher + MORSE_CODE.get(i, i) + ' '
        else:
            cipher += ' '
    return cipher

# FUNCTION TO DECODE MESSAGE


def decode(message):
    decipher = ''
    message = message.split()

    for i in message:
        decipher += LETTERS[MORSE_VALUES.index(i)] + ''

    # I CONVERTED THE MESSAGE INTO A LIST USING THE SPLIT METHOD
    # THEN GOT THE INDEX OF THE MORSE_VALUES IN THE MORSE_VALUES LIST
    # SINCE THE INDEX OF THE MORSE_VALUES AND THE LETTERS WOULD BE THE SAME,
    # I GOT THE INDEX OF THE CHARACTER IN THE MESSAGE FROM THE MORSE_VALUES
    # THEN I USED THAT SAME INDEX TO GET THE INDEX OF THE LETTERS, IN PLAIN ENGLISH

    # MESSAGE MUST BE IN MORSE CODE, ELSE WOULD GET A VALUE ERROR ERROR

    return decipher


# FUNCTION TO CHECK IF FILE EXISTS
def file_exists(filename):
    # YOU CAN USE ABSOLUTE FILE PATH (c:\\users\\filename) OR JUST THE FILENAME (filename.txt)
    return os.path.exists(filename)


# FUNCTION TO READ LINES OF FILE
def read_lines(mode, filename):
    with open(filename, 'r') as file:       # OPEN FILE
        # READ FILE CONTENTS AND STORE THEM IN "CONTENT" VARIABLE
        content = file.read()
    # IF MODE IS encode (e), RETURN ENCODED MESSAGE
    if mode == 'e':
        return encode(content)
    elif mode == 'd':                       # ELSE RETURN DECODED CONTENT OF MESSAGE
        return decode(content)
    else:                                   # IF MODE IS NOT VALID...
        return "Invalid mode!, Try again"


def print_intro():
    print("Welcome to Wolmorse")
    print("This program encodes and decodes Morse code.")
    get_input()


# print(encode('derron is great'))
# print(decode('-.. . .-. .-. --- -.  .. ...  --. .-. . -... - '))


# MAIN METHOD
def main():
    print_intro()


# IF FILE IS IMPORTED OR RUN DIRECTLY FROM THE COMMAND LINE OR PYTHON SHELL, RUN THE MAIN METHOD
if __name__ == '__main__':
    main()
