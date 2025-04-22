import socket
import os

SOCKET_PATH = "/tmp/unix_socket"

# Remove previous socket file if it exists
if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

# Create the server socket
server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_socket.bind(SOCKET_PATH)
server_socket.listen(5)
print(f"Server listening on {SOCKET_PATH}")

try:
    while True:
        conn, _ = server_socket.accept()
        print("Client connected")

        # Handle client communication
        data = conn.recv(1024)
        if not data:
            print("Client disconnected")
            conn.close()
            continue

        print(f"Received: {data.decode()}")

        # Send response
        response = "Hello from server"
        conn.sendall(response.encode())

        conn.close()

except KeyboardInterrupt:
    print("\nServer shutting down...")

# Clean up
server_socket.close()
os.remove(SOCKET_PATH)
