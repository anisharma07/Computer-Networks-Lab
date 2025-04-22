import socket

SOCKET_PATH = "/tmp/unix_socket"

# Create socket
client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(SOCKET_PATH)

# Send message
message = "Hello from client"
client_socket.sendall(message.encode())

# Receive response
data = client_socket.recv(1024)
print(f"Server response: {data.decode()}")

# Clean up
client_socket.close()
