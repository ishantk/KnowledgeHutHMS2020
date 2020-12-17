"""
    Socket Programming
        Write Distributed Applications
"""
# Server Program
import socket

def help():
    print("Need some help")

def sleep(seconds):
    import time
    time.sleep(seconds)

commands = {
    "help": help,
    "sleep": sleep
}

host = "127.0.0.1"
port = 12345

# Create a Socket Object
server = socket.socket()

# bind the Socket to Host and Port
server.bind((host, port))

# Listen for any incoming data
server.listen()

# accept the connection from some client
connection, address = server.accept()
print("[SERVER] Connection Accepted From {}".format(str(address)))

while True:
    data = connection.recv(1024).decode()

    if not data:
        break

    print("[SERVER] Data from Client")
    print(str(data))

    data = str(data).upper()
    print("[SERVER] MESSAGE from Client", data)

    text_message = input("[SERVER] Enter Some Message for Client: ")
    connection.send(text_message.encode())


connection.close()
print("[SERVER] Connection Terminated")