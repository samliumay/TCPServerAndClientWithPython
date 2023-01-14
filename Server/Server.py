from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print('The server is ready to Service')
while True:
    connectionSocket, addr = serverSocket.accept()
    print('A message came...')
    sentence = connectionSocket.recv(1024).decode()
    newSentence = sentence.upper()
    connectionSocket.send(newSentence.encode())
    connectionSocket.close()
    print('Updated Massage sent...')