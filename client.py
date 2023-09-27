#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
welcomeMessage = "Welcome to the Equilateral Triangle calculator"

print("Client starting - connecting to server at IP", HOST, "and port", PORT)

#creates a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))#establish connection
    print(f"Connection established, sending message: '{welcomeMessage}'")
    s.sendall(bytes(welcomeMessage, 'utf-8'))#send message

    #Enter side length and send
    side_length = float(input("Enter the length of the sides: "))
    s.sendall(str(side_length).encode())

    #Makes sure the user selects the correct operation and send
    operation = ''
    while operation != 'p' and operation != 'a':
        operation = input("Enter 'a' to calculate area or 'p' to calculate perimeter: ").lower()

    s.sendall(operation.encode())
    print("Messages sent, waiting for reply")


    data = s.recv(1024)#get data

print(f"Received response: '{data!r}' [{len(data)} bytes]")
print("Client is done!")
