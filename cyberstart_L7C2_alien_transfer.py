# Cybestart Level 7 Challenge 2 - 'Alien Transfer'

# Set up a server listening on localhost, port 10000, to intercept one of alien messages.
# When you do, permofm a bitwise XOR on the message with the key "attackthehumans"
# and then respond with the encrypted data.

# Tip: Read the response to get the flag.

import socket

# I create a socket object:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# I define the host and the port:
host = "localhost"
port = 10000

# I bind to the port:
s.bind((host,port))

# Now I wait for client connection.
s.listen(5)
print(f"Server is listening on {host}:{port}")

while True:
    # I establish connection with the client:
    c, addr = s.accept()
    print(f"Connection established from {addr}")

    # I receive data from the client:
    data = c.recv(1024).decode("utf-8")
    print(f"Received data: {data}")

    # XOR the data with the key "attackthehumans"
    key = "attackthehumans"
    xor_data = xor_with_key(data, key)
    print(f"XORed data: {data}")

    # I send XORed data back to the client:
    c.send(xor_data.encode("utf-8"))

    # I close the connection:
    c.close()