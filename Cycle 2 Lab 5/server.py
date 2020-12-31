from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))

print("Server is Up & is Ready to Receive the Request from the CLients: ")

while 1:
    sentence, clientAddress = serverSocket.recvfrom(2048)
    file = open(sentence, "r")
    I = file.read(2048)
    serverSocket.sendto(bytes(I, "utf-8"), clientAddress)
    print("Sent Back to Client")
    file.close()
