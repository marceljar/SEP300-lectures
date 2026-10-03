import socket

HOST = "127.0.0.1"   # Server's hostname or IP
PORT = 65435         # Same port as the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) \
                                          as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected to server")
    client_socket.sendall(b"Hello World")
