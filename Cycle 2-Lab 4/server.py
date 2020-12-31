from socket import *

serverName = "127.0.0.1"
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))

serverSocket.listen(1)
print("Server is Up & Ready to Receive the Request From the Client: ")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    file = open(sentence, "r")
    I = file.read(1024)
    connectionSocket.send(I.encode())
    file.close()
    connectionSocket.close()
