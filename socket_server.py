"""
THIS IS THE SERVER
"""

import socket                                               # socket is the library for performing socket programming
import select
import sys
import _thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host_name = socket.gethostname()
host_IP = socket.gethostbyname(host_name)
print(f"This is the server called {host_name} @ {host_IP}")                                          # Get the private IP from the name of the host

port = 8920         # Probably i can change this manually


server.bind((host_IP, port))

server.listen(100)                         # set how many clients can the server accept simultaneously

list_of_clients = []
list_of_IP_connected = []


def clientthread(conn, addr):
    conn.send_data(bytes("Welcome to this chat-room!", "utf-8"))      # send a message of welcome to the client just entered in the chat
    while True:
        try:
            message = conn.recv(2048).decode()
            if message:
                print(f"{addr[0]} said: {message}")
                message_to_send = f"{addr[0]} said: {message}"
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:       # The user who sent the message does not need to receive the message
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:

    conn, addr = server.accept()

    list_of_clients.append(conn)
    list_of_IP_connected.append(addr)
    print(list_of_IP_connected)
    print(f"The user {addr[0]} has connected")
    _thread.start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
