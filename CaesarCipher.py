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

def main():
    # Generate a random key
    key = getRandomNum()

    # Save key to a file for decryption
    with open("key.txt", "w") as keyFile:
        keyFile.write(str(key))

    # Prompt user for a message
    message = input("Please enter message to be encrypted: ")

    # Encrypt the message
    encryptedMessage = caesarCipher(message, key)
    print(f"Encrypted message: {encryptedMessage}")

    # Save encrypted message to a file
    with open("encrypted.txt", "w") as encFile:
        encFile.write(encryptedMessage)

    # Decryption process
    with open("key.txt", "r") as keyRead:
        savedKey = int(keyRead.read())

    with open("encrypted.txt", "r") as encRead:
        encryptedText = encRead.read()

    decryptedMessage = caesarDecipher(encryptedText, savedKey)
    print(f"Decrypted message: {decryptedMessage}")

if __name__ == "__main__":
    main()
