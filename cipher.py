# Goal: Create an app that encodes/decodes a message by using an OTP Cipher.

import secrets

# ------------ Request user input. ------------ #

# IMPORTANT: Comment the following if you have a message file and pad file.
message = input("Please enter a message you want to encrypt: ")
padLength = int(input("Please pick a Pad length longer than the message: "))

# IMPORTANT: Comment the following if you are inputting a message and need to generate a pad.
# filename = input("Please enter a filename you want to encrypt/decrypt: ")
# filenamePAD = input("Please enter a filename for the pad of the file you want to decrypt: ")

# Open the file in read mode and importing contents.
# IMPORTANT: Comment the following if you are inputting a message and need to generate a pad.
# file = open(filename, "r")
# message = file.read()


# ------------ Functions. ------------ #

# Function that generates a random pad, converts the characters into 
# ASCII values, then adds them to a list.
# ^[https://inventwithpython.com/cracking/chapter21.html].

def generatePad(padLength, ascii_pad):
    otp = ''
    for i in range(padLength):
        otp += secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    for c in otp:
        ascii_pad.append(ord(c))
    
    return ascii_pad


# Function that converts characters of message to ASCII values 
# and puts them in a list.
# ^ [https://www.delftstack.com/howto/python/convert-string-to-ascii-python/#:~:text=Use%20the%20for%20Loop%20Along%20With%20the%20ord,function%20returns%20the%20Unicode%20of%20the%20passed%20string].
def calcShift(message, ascii_message):

    for c in range(len(message)):
        c = ord(message[c])
        ascii_message.append(c)
    return ascii_message


# Function that encrpyts the message.
def encipher(ascii_message, ascii_pad, new_message):
    # Truncate pad to size of message.
    l = len(ascii_message)
    shortPad = ascii_pad[0:l]

    # Shift a letter in message by a letter value one-time pad, 
    # regardless of case.
    # ^[https://stackoverflow.com/questions/4838504/how-do-i-truncate-a-list].
    for i in ascii_message:
        j = 0
        if (i >= 65) and (i <= 90):
            shifted = (i - 65 + shortPad[j] - 65) % 26 + 65
            j += 1
        elif (i >= 97) and (i <= 122):
            shifted = (i - 97 + shortPad[j] - 65) % 26 + 97
            j += 1
        else:
            shifted = i
        new_message.append(chr(shifted))
    return ''.join(new_message)


# Function that decrypts the messages.
def decipher(aMessage, ascii_pad, old_message):
    # aMessage is a variable for the input of the user's message or 
    # the message filename (variables 'message' or 'filename'). 
    # When running the functions, you chooese what aMessage is. 
    encryptedList = []
    for i in range(len(aMessage)):
        i = ord(aMessage[i])
        encryptedList.append(i)

    # Truncate pad to size of message.
    l = len(encryptedList)
    shortPad = ascii_pad[0:l]
    
    j = 0   # j references the index of the ASCII values for the pad.
    for i in encryptedList:
        if (i >= 65) and (i <= 90):
            shifted = (i - 65 - shortPad[j] - 65) % 26 + 65
            j += 1
        elif (i >= 97) and (i <= 122):
            shifted = (i - 97 - shortPad[j] - 65) % 26 + 97
            j += 1
        else:
            shifted = i
        old_message.append(chr(shifted))
    return ''.join(old_message)

# Empty lists for functions.
new_message = []
old_message = []
ascii_message = []
ascii_pad = []

# ------------ End Functions. ------------ #


# For given pad file, read it and turn it into list of ASCII values.
# IMPORTANT: Comment the following lines if you are generating a pad. 

# padfile = open(filenamePAD, "r")
# pad = padfile.read()

# for i in pad:
#     ascii_pad.append(ord(i))


# ------------ Call the functions. ------------ #

generatePad(padLength, ascii_pad)
calcShift(message, ascii_message)
print(encipher(ascii_message, ascii_pad, new_message))
print(decipher(encipher(ascii_message, ascii_pad, new_message), ascii_pad, old_message))
# print(decipher(message, ascii_pad, old_message))