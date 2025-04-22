import socket

# Replace with your server's IP address
SERVER_IP = "192.168.80.129"   # Change this to server's IP
PORT = 5004

# Create and connect the socket

try:
    while True:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, PORT))

        # Get user input
        message = input("Enter message: ")
        if message.lower() == 'exit':
            print("Exiting...")
            break

        # Send message
        client_socket.sendall(message.encode())

        # Receive response
        data = client_socket.recv(1024)
        print(f"Server: {data.decode()}")
finally:
    # Clean up
    client_socket.close()