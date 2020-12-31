from socket import *

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Enter the Filename: ")
clientSocket.send(sentence.encode())
fileContents = clientSocket.recv(1024).decode()
print("From Server: ", fileContents)

clientSocket.close()