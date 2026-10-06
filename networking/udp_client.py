import socket

HOST = "127.0.0.1"
PORT = 65431

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) \
                                           as client_socket:
    client_socket.sendto("Hello".encode("utf-8"), (HOST, PORT))
    client_socket.settimeout(2.0)  # avoid waiting forever
    data, _ = client_socket.recvfrom(1024)
    print("Received from server:", data.decode("utf-8"))
