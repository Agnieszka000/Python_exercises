# The script is based on The Complete Python Hacking Course on O'Reilly platform,
# but rewritten in Python 3 and enhanced.
# It scans one port at a time.

# Specify the path to the libraries to be used:
#!/usr/bin/python

# Import a library that allows to connect to target ports:
import socket

# Create a socket:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set the timeout to 2 seconds:
socket.setdefaulttimeout(2)

# socket.AF_INET ==> IPv4 address
# socket.SOCK_STREAM ==> it stands for TCP packets

host = input("[*] Write the IP address: ")
port = int(input("[*] Write the port number: "))


# Connect:
def portscanner(port):
    try:
        sock.connect((host,port))
        print(f"Port {port} is open.")
    except ConnectionRefusedError:
        print(f"Port {port} is closed.")
    except socket.timeout:
        print(f"Timeout!")
    except socket.error as err:
        print(f"Port {port}: {err}")
    # Close the socket!!!
    finally:
        sock.close()

portscanner(port)