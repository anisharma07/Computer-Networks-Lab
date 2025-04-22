import socket
import threading


HOST = "0.0.0.0"  
PORT = 5003        

clients = []

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn: 
            try:
                client.sendall(message)
            except Exception as e:
                print(f"Error sending to client: {e}")
                clients.remove(client)

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"Connection closed by {addr}")
                break
            print(f"Received from {addr}: {data.decode()}")

            broadcast(data, conn)
    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        clients.remove(conn)  
        conn.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")

try:
    while True:
        
        conn, addr = server_socket.accept()

        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

except KeyboardInterrupt:
    print("\nServer shutting down...")

server_socket.close()