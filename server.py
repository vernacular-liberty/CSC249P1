import socket
import math

HOST = "127.0.0.1"
PORT = 65432

print("Server starting - listening for connections at IP", HOST, "and port", PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")

        while True:
            welcomeMessage = conn.recv(1024)
            if not welcomeMessage:
                break
            print(f"Received client message: '{welcomeMessage.decode()}' [{len(welcomeMessage)} bytes]")

            side_length = conn.recv(1024)
            if not side_length:
                break
            print(f"Received client side length: '{side_length!r}' [{len(side_length)} bytes]")
            side_length = float(side_length)

            operation = conn.recv(1024)
            if not operation:
                break
            print(f"Received client operation: '{operation.decode()}' [{len(operation)} bytes]")
            operation = operation.decode()

            if operation == "a":
                result = (math.sqrt(3) / 4) * side_length**2
            elif operation == "p":
                result = 3 * side_length
            else:
                result = "Invalid choice"

            conn.sendall(str(result).encode())
            
print("Server is done!")
