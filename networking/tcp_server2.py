import socket

HOST = "127.0.0.1"   # Localhost
PORT = 65434         # Port to listen on
MAX = 1              # MAximum number of queued connections

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) \
                                           as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(MAX)

    while True:
        print("Server is listening...")
        conn, addr = server_socket.accept()
        with conn:
            print("Connection achieved")
            data = conn.recv(1024)
            if data:
                print("From client:", data.decode("utf-8"))
                feedback = "Message received successfully!"
                conn.sendall(feedback.encode("utf-8"))
            print("Connection closed")
        
