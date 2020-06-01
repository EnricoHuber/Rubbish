"""
THIS IS THE CLIENT
"""


import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


IP_address = socket.gethostbyname(socket.gethostname())
port = 8920


client_socket.connect((IP_address, port))

while True:
    sockets_list = [client_socket]
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets + [sys.stdin]:
        if socks == client_socket:
            message = socks.recv(2048)
            print(message)
        else:
            message = sys.stdin.readline()
            client_socket.send(bytes(message, "utf-8"))
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()

client_socket.close()