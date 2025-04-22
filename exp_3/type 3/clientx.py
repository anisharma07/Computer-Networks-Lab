import socket

# Server configuration (replace with server's IP address)
SERVER_IP = "192.168.189.61"  # Use the server's IP
SERVER_PORT = 5000

# Create and connect the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))

try:
    message = "Hello, Server!"
    print("Sending:", message)
    client_socket.sendall(message.encode())

    response = client_socket.recv(1024)
    print("Response from server:", response.decode())

finally:
    client_socket.close()
