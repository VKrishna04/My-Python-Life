import socket
import threading


# Function to receive messages from the server
def receive_messages(client_socket) -> None:
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Server: {message}")
        except ConnectionResetError:
            print("Server disconnected.")
            break


# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12346))

# Use threading to receive messages continuously
receiver_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receiver_thread.start()

# Send messages to the server continuously
while True:
    message = input("Client: ")
    client_socket.send(message.encode("utf-8"))

    if message.lower() == "exit":
        print("Disconnected from the server.")
        break

client_socket.close()
