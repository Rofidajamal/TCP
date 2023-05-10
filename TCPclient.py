from socket import *
serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
connection = True
while connection :
    message = input('Enter your message or Exit :   ')
    clientSocket.send(message.encode())
    received = clientSocket.recv(1024).decode()
    print('message received From Server:  ', received)
    if message == "Exit":
        print("Now you are diconecting from server")
        connection = False
        break


