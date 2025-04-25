import socket

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

try:
    while True:
        conn, addr = server_socket.accept()
        print(addr)

        while True:
            data = conn.recv(1024)
            if not data:
                print("no data")
            else:
                print(data.decode())
                conn.sendall("Message Recieved")

        conn.close()

except KeyboardInterrupt:
    print("\nServer shutting down.")

finally:
    server_socket.close()
