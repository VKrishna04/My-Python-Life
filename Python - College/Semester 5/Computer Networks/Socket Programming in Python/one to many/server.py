import socket
import threading

# Server configuration
HOST = "127.0.0.1"
PORT = 12346

# List to keep track of connected clients
clients = []


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"Received message: {message}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue


def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode("utf-8"))
            except:
                remove(client)


def remove(connection):
    if connection in clients:
        clients.remove(connection)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        print(f"Connection established with {client_address}")

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


if __name__ == "__main__":
    main()
