import random

# Function to generate a random key
def getRandomNum():
    return random.randint(32, 126)

# Function to encrypt message
def caesarCipher(text, shift):
    encryptedText = ""
    for c in text:
        if 32 <= ord(c) <= 126:
            encryptedText += chr(((ord(c) - 32 + shift) % 95) + 32)
        else:
            encryptedText += c
    return encryptedText

# Function to decrypt message
def caesarDecipher(message, shift):
    decryptedText = ""
    for c in message:
        if 32 <= ord(c) <= 126:
            decryptedText += chr(((ord(c) - 32 - shift + 95) % 95) + 32)
        else:
            decryptedText += c
    return decryptedText
