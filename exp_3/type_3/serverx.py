import socket

# Server configuration
SERVER_IP = "0.0.0.0"  # Listen on all available network interfaces
SERVER_PORT = 5000

# Create and bind the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

try:
    while True:
        # Accept a new client connection
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Communication with the client
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"Client {addr} disconnected")
                break  # Exit the inner loop when the client disconnects

            print(f"Received from {addr}: {data.decode()}")
            conn.sendall(b"Message received")

        conn.close()  # Close only the client connection, not the server socket

except KeyboardInterrupt:
    print("\nServer shutting down.")

finally:
    server_socket.close()
