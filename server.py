from socket import *
from CaesarCipher import caesarDecipher

def server():
    serverPort = 12345

    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(("",serverPort))
    serverSocket.listen(1)

    print ("The Server running over TCP is ready to receive ... ")
    
    while 1:
        connectionSocket, addr = serverSocket.accept()
        print(f"Connection established with {addr}")
        
        try:
            # Receive key from client
            key = int(connectionSocket.recv(1024).decode())
            print(f"Received key: {key}")
            
            # Receive encrypted message
            encryptedMessage = connectionSocket.recv(1024).decode()
            print(f"Received encrypted message: {encryptedMessage}")
            
            # Decrypt the message
            decryptedMessage = caesarDecipher(encryptedMessage, key)
            print(f"Decrypted message: {decryptedMessage}")

            # Send acknowledgment
            connectionSocket.send("Message received and decrypted.".encode())

        except Exception as e:
            print(f"Error occurred: {e}")
        
        finally:
            connectionSocket.close()

    serverSocket.close()
 
if __name__ == "__main__":
    server()