from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print('Write your massage to the server')
message = input()
clientSocket.send(message.encode())

modifiedMessage = clientSocket.recv(1024)
print('From Server: ' , modifiedMessage.decode())
clientSocket.close()
