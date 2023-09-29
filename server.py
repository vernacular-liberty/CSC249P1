import socket
import math

HOST = "127.0.0.1"
PORT = 65432

#establish server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server starting - listening for connections at IP", HOST, "and port", PORT)
    
    #search for connections
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")

        while True:
            welcomeMessage = conn.recv(1024)
            if not welcomeMessage:
                break
            print(f"Received client message: '{welcomeMessage.decode()}' [{len(welcomeMessage)} bytes]")

            sides = conn.recv(1024)
            if not sides:
                break
            print(f"Received client sides amount: '{sides!r}' [{len(sides)} bytes]")
            sides = int(sides)

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
                if sides == 3:
                    result = (math.sqrt(3) / 4) * side_length**2
                    shape = "triangle"
                elif sides == 4:
                    result = side_length**2
                    shape = "square"
                elif sides == 5:
                    result = (1/4) * (5 * (5 + 2 * math.sqrt(5))) * side_length**2
                    shape = "pentagon"
                elif sides == 6:
                    result = ((3 * math.sqrt(3))/2) * side_length**2
                    shape == "hexagon"
                elif sides == 7:
                    result = (7/4) * side_length**2 * (1 / math.tan(math.pi/7))
                    shape = "heptagon"
                else:
                    result = "This shape is not available yet."
            elif operation == "p":
                result = sides * side_length
            else:
                result = "Invalid operation choice"

            conn.sendall(str(result).encode())
            conn.sendall(shape.encode())
            
print("Server is done!")
