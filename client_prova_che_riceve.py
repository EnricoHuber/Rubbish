"""
THIS IS THE CLIENT
"""


import socket

host = socket.gethostbyname(socket.gethostname())
port = 8920                                     # here client needs the server's port
client_socket = socket.socket()                 # instantiate client socket

client_socket.connect((host, port))             # connect client to server
print(client_socket.recv(2048).decode())


while True:
    data = client_socket.recv(1024).decode()    # receive a message from the server

    print(f"Received from server: {data}")


print("Connection closed!")
client_socket.close()                           # close connection

