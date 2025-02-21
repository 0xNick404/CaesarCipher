from socket import *
from CaesarCipher import caesarDecipher

def server():
    serverPort = 12345

    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(("",serverPort))
    serverSocket.listen(1)

    print ("The Server running over TCP is ready to receive ... ")
    
    try:
        while True:
            try:
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
                    print(f"Error occurred during processing: {e}")
                    connectionSocket.send("Error processing message.".encode())
                    
            except Exception as e:
                    print(f"Connection accept error: {e}")
            
            finally:
                connectionSocket.close()
                
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        
    finally:    
        serverSocket.close()
 
if __name__ == "__main__":
    server()