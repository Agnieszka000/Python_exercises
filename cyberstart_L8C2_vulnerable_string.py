# Cyberstart Platform - Level 8, Challenge 2 - "Vulnerable String"

# Write a script which can connect to the following server
# 'localhost':10000 over TCP, and send 'GET_KEY' to download the string.
# The string is compressed withe a common algorithm found in many
# websites. Decompress the string and print it to get the flag.

import socket
import gzip

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost", 10000))

clientsocket.send("GET KEY".encode())

data = clientsocket.recv(1024)
decompressed_data = gzip.decompress(data)
print(decompressed_data)