"""
    Socket Programming
        Write Distributed Applications
"""
# Client Program

import socket

host = "127.0.0.1"
port = 12345

client = socket.socket()

client.connect((host, port))

text_message = input("[CLIENT] Enter Your Message: ")
while text_message != 'q':
    client.send(text_message.encode())

    data = client.recv(1024).decode()
    print("[CLIENT] Data Received from Server", data)

    text_message = input("[CLIENT] Enter Your Message: ")

client.close()