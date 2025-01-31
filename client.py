from socket import *
from CaesarCipher import getRandomNum, caesarCipher

def client():
    serverName = "127.0.0.1"
    serverPort = 12345
    
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))

        # Prompt user for a message
        message = input("Please enter message to encrypt and send: ")
        
        # Generate a random key
        key = getRandomNum()
        
        # Encrypt the message
        encryptedMessage = caesarCipher(message, key)
        
        # Send the key
        clientSocket.send(str(key).encode())
        
        # Send encrypted message
        clientSocket.send(encryptedMessage.encode())

        # Receive acknowledgment from server
        response = clientSocket.recv(1024).decode()
        print(f"Server response: {response}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        clientSocket.close()
    
if __name__ == "__main__":
    client()