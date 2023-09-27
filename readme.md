# Equilateral Triangle Calculator - Client-Server Message Format Documentation

This documentation describes the message format and communication protocol used in the Equilateral Triangle Calculator client-server application. The document provides an overview of the application, details on client-to-server and server-to-client message formats, examples of expected output, and acknowledgments.

## Overview of Application

### Purpose
The client-server application is designed to calculate properties (area or perimeter) of an equilateral triangle. It involves a server that listens for connections and a client that connects to the server. The client sends information about the triangle's side length and the desired calculation (area or perimeter) to the server. The server performs the calculation and sends the result back to the client.

### Components
- **Server**: Listens for client connections, receives data, performs calculations, and sends responses.
- **Client**: Establishes a connection to the server, sends data, and receives results.

## Client->Server Message Format

### 1. Welcome Message
- **Description**: The client sends a welcome message to the server when establishing a connection.
- **Components**:
  - A string message (UTF-8 encoded) to greet the server.
- **Example**:
  - Client sends: "Welcome to the Equilateral Triangle calculator."

### 2. Side Length
- **Description**: The client sends the length of the sides of the equilateral triangle to the server.
- **Components**:
  - A floating-point number representing the side length.
- **Example**:
  - Client sends: "5.0" (encoded as a UTF-8 string).

### 3. Operation Selection
- **Description**: The client selects the operation they want to perform (area or perimeter) and sends it to the server.
- **Components**:
  - A single character: 'a' for area or 'p' for perimeter.
- **Example**:
  - Client sends: "a" (encoded as a UTF-8 string).

### 4. Result Request
- **Description**: The client sends a request for the calculation result to the server.
- **Components**:
  - No data; it's a control message.
- **Example**:
  - No data is sent; it's a signal to the server.

## Server->Client Message Format

### 1. Welcome Message
- **Description**: The server sends a welcome message to greet the client and inform them about the server's purpose.
- **Components**:
  - A string message (UTF-8 encoded) as a greeting.
- **Example**:
  - Server sends: "Welcome to the Equilateral Triangle calculator."

### 2. Side Length
- **Description**: The server receives the side length of the equilateral triangle from the client.
- **Components**:
  - A floating-point number representing the side length.
- **Example**:
  - Server receives: "5.0" (decoded from a UTF-8 string).

### 3. Operation Request
- **Description**: The server requests the client to specify whether they want to calculate the area or perimeter of the equilateral triangle.
- **Components**:
  - A string message instructing the client to enter 'a' for area or 'p' for perimeter.
- **Example**:
  - Server sends: "Enter 'a' to calculate area or 'p' to calculate perimeter."

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

### Client-Server Interaction Example
- **Client**:
  1. Connects to the server.
  2. Sends the welcome message: "Welcome to the Equilateral Triangle calculator."
  3. Sends the side length: "5.0".
  4. Sends the operation selection: "a".
  5. Requests the result.

- **Server**:
  1. Accepts the client's connection.
  2. Receives the welcome message: "Welcome to the Equilateral Triangle calculator."
  3. Receives the side length: "5.0".
  4. Requests the operation: "Enter 'a' to calculate area or 'p' to calculate perimeter."
  5. Calculates the area (result: "15.0") and sends it to the client.

- **Client**:
  - Receives the result: "15.0".

### Error Example
- **Client**:
  1. Connects to the server.
  2. Sends the welcome message: "Welcome to the Equilateral Triangle calculator."
  3. Sends an invalid operation: "x".

- **Server**:
  1. Accepts the client's connection.
  2. Receives the welcome message: "Welcome to the Equilateral Triangle calculator."
  3. Receives an invalid operation: "x".
  4. Sends an error message: "Invalid choice".

- **Client**:
  - Receives the error message: "Invalid choice".

## Acknowledgments

This client-server message format documentation provides a clear understanding of the communication protocol used in the Equilateral Triangle Calculator application. It ensures that a competent programmer can create a client or server that communicates properly with the existing implementation.
