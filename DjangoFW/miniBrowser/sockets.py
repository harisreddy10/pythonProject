import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to your server
server_address = ('localhost', 9211)  # Use the address and port of your server
client_socket.connect(server_address)

# Send an HTTP GET request
request = "GET / HTTP/1.1\r\nHost: localhost:9211\r\n\r\n"
client_socket.send(request.encode())

# Receive and print the response
response_data = b"" #this form of empty string recieves utf-8(byte format)
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    response_data += data

# Print the response as a string
print(response_data.decode())

# Close the client socket
client_socket.close()
