import socket

serverIP = '198.61.28.1'
serverPort = 5000

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((serverIP, serverPort))

try:
    messgage = "hello server"
    clientsocket.sendall(message.decode())
    response = clientsocket.recv(1024)
    response.decode()


finally:
    clientsocket.close()
