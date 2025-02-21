import random

# Function to generate a random key
def getRandomNum():
    return random.randint(0, 127)

# Function to encrypt message
def caesarCipher(text, shift):
    encryptedText = ""
    for c in text:
        encryptedText += chr(((ord(c) + shift) % 128))
    return encryptedText

# Function to decrypt message
def caesarDecipher(message, shift):
    decryptedText = ""
    for c in message:
        decryptedText += chr(((ord(c) - shift + 128) % 128))
    return decryptedText
