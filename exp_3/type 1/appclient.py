import socket
import threading


SERVER_IP = "192.168.80.61"  
PORT = 5003


def receive_messages(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print("Disconnected from server.")
                break
            print(f"\nServer: {data.decode()}")
    except Exception as e:
        print(f"Error receiving data: {e}")
    finally:
        client_socket.close()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))


receiver_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receiver_thread.daemon = True 
receiver_thread.start()

try:
    while True:
        
        message = input("Enter message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            print("Exiting...")
            break


        client_socket.sendall(message.encode())
finally:
    
    client_socket.close()