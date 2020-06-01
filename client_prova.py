"""
THIS IS THE CLIENT
"""


import socket

host = socket.gethostbyname(socket.gethostname())
port = 8920                                     # here client needs the server's port
client_socket = socket.socket()                 # instantiate client socket

client_socket.connect((host, port))             # connect client to server
print(client_socket.recv(2048).decode())

message = input("  ->  ")                       # take an input

while message.lower().strip() != 'bye':         # la connessione resta aperta finché il client non scrive 'bye'
    client_socket.send(message.encode())        # send message to server
    data = client_socket.recv(1024).decode()    # receive a message from the server

    print(f"Received from server: {data}")

    message = input("  ->  ")                   # take another message, type 'bye' to exit

print("Connection closed!")
client_socket.close()                           # close connection

