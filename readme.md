# Equilateral Triangle Calculator - Client-Server Message Format Documentation

## Overview of Application

### Purpose
The client-server application is designed to calculate properties (area or perimeter) of an equilateral triangle. The client sends information about the triangle's side length and the desired calculation (area or perimeter) to the server. The server performs the calculation and sends the result back to the client.

## Client->Server Message Format

### 1. Welcome Message
- **Description**: The client sends a welcome message in the form of a UTD-* encoded string to the server when establishing a connection. This is not needed, but good for practice.

### 2. Side Length
- **Description**: The client sends the length of the sides of the equilateral triangle in the form of a float to the server.
  
### 3. Operation Selection
- **Description**: The client selects the operation they want to perform (area or perimeter) as a single character, 'a' or 'p', and sends it to the server. Also encoded as a UTF-8 string.

### 4. Result Request
- **Description**: The client sends a request in the form of a signal for the calculation result to the server.

## Server->Client Message Format

### 1. Welcome Message
- **Description**: The server sends a welcome message in the form of a UTD-* encoded string to the server when establishing a connection.
  
### 2. Side Length
- **Description**: The server receives the float, side length of the equilateral triangle from the client.

### 3. Operation Request
- **Description**: The server uses a signal to request the client to specify whether they want to calculate the area or perimeter of the equilateral triangle.

### 4. Result
- **Description**: The server calculates the requested result (either area or perimeter) and sends it to the client as a response.
- **Components**:
  - The result, which can be:
    - A floating-point number (e.g., area or perimeter value).
    - A string message indicating an invalid choice.
- **Example**:
  - Server sends: "15.0" (encoded as a UTF-8 string) for the area calculation result.
  - Server sends: "Invalid choice" (encoded as a UTF-8 string) for an invalid operation.

## Example Output

### Ex1
  1. Input Side Length: 4
  2. Input Operation: a
  3. Output: 6.9282
     
- Ex2
  1. Input Side Length: 5
  2. Input Operation: p
  3. Output: 15

## Client Trace


## Server Trace


## Acknowledgments
  - Socket Programming in Python (Guide) by Nathan Jennings [https://realpython.com/python-sockets/]
