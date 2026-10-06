import socket

HOST = "127.0.0.1"   # Server's hostname or IP
PORT = 65434         # Same port as the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) \
                                           as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected to server")
    message = input("Enter Message to be transmitted: ")
    client_socket.sendall(message.encode("utf-8"))
    data = client_socket.recv(1024)
    if data:
        print("Message from Server:", data.decode("utf-8"))
        