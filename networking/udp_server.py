import socket

HOST = "127.0.0.1"   # Localhost
PORT = 65431         # Port to listen on
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) \
                                         as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}")

    while True:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)

        message = data.decode("utf-8")
        print(f"Message from {addr}: {message}")

        feedback = "Message received successfully!"
        server_socket.sendto(feedback.encode("utf-8"), addr)
