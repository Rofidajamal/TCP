from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
ServerAdd = serverSocket.getsockname()
ExitMessage = "Exit"
connection = True
while True:
    connectionSocket, addr = serverSocket.accept()
    print("The server is lestining at ", f"{ServerAdd}")
    print("The server is connected to : ", f"{addr}")
    print("The socket coneects between ", f"{ServerAdd}", " and  ", f"{addr}")
    while connection:
        data = connectionSocket.recv(1024).decode()
        print ("Message from the Client: ", data)
        if data == ExitMessage:
            m = "Disconnect!"
            connectionSocket.send(m.encode())
            print ("Reply sent,Server socket closed" )
            print ("Listening at ", f"{ServerAdd}")
            connection = False
        else:
            dataLen = len(data)
            message = "Your data was " + f"{dataLen}" + " bytes"
            connectionSocket.send(message.encode())


    connectionSocket.close()



