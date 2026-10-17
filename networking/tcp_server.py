import socket

HOST = "127.0.0.1"   # Localhost
PORT = 65432         # Port to listen on
MAX = 1              # Maximum number of queued connections

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) \
                                          as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX)
    print("Server is listening...")

    conn, addr = server_socket.accept()
    with conn:
        print("Connection achieved")
        data = conn.recv(1024)
        if data:
            print("Message from client:", data.decode())
        print("Connection closed")
