#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
welcomeMessage = "Welcome to the Regular Shape calculator"

print("Client starting - connecting to server at IP", HOST, "and port", PORT)

#creates a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))#establish connection
    print(f"Connection established, sending message: '{welcomeMessage}'")
    s.sendall(bytes(welcomeMessage, 'utf-8'))#send message

    #Enter number of sides
    sides = 1
    while sides < 2 or sides > 8:    
        sides = int(input("Enter the number of sides between 3-7: "))
    s.sendall(str(sides).encode())

    #Enter side length and send
    side_length = float(input("Enter the length of the sides: "))
    s.sendall(str(side_length).encode())

    #Makes sure the user selects the correct operation and send
    operation = ''
    while operation != 'p' and operation != 'a':
        operation = input("Enter 'a' to calculate area or 'p' to calculate perimeter: ").lower()

    s.sendall(operation.encode())
    print("Messages sent, waiting for reply")

    data = s.recv(1024)  # Receive the result first
    shape = s.recv(1024)  # Then receive the shape

print(f"Received server data response: '{data!r}' [{len(data)} bytes]")
print(f"Received server shape response: '{shape!r}' [{len(shape)} bytes]")

if operation == 'a':
    print(f"The area of a {shape} with {sides} sides is {data} units squared.")
elif operation == 'p':
    print(f"The perimeter of a {shape} with {sides} sides is {data} units.")

