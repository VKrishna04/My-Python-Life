import socket
import threading


# Function to handle client messages
def handle_client(client_socket):
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode("utf-8")
            if not message or message.lower() == "exit":
                print("Client disconnected.")
                break
            print(f"Client: {message}")

            # Send a response back to the client
            response = input("Server: ")
            client_socket.send(response.encode("utf-8"))

            if response.lower() == "exit":
                print("Closing connection.")
                break

        except ConnectionResetError:
            print("Client disconnected abruptly.")
            break

    client_socket.close()


# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12346))
server_socket.listen(1)
print("Server listening on port 12346")

# Accept incoming connections
client_socket, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Use threading to handle the client in a separate thread
client_handler = threading.Thread(target=handle_client, args=(client_socket,))
client_handler.start()
