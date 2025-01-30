# CyberStart Level 3 Challenge 2: Sockets & Servers

# Write a TCP Client that will connect to 127.0.0.1 on port 9990.
# Your client must send "Knock, knock" to the server.
# Then get the response, and print it out.

# Import the socket library.
import socket

# To make a connection to a TCP server:

# Create a socket. AF_INET means we're connecting to an IPv4 IP address.
# SOCK_STREAM means we're connecting over TCP and not UDP.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tell the socket what IP address and port number to connect to.
clientsocket.connect(('127.0.0.1', 9990))

# Send data over the socket.
clientsocket.send("Knock, knock".encode())

# Receive data back. The 1024 is the max number of bytes of data to accept.
data = clientsocket.recv(1024)
print(data)