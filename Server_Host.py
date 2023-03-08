import time, socket, sys
from dataclasses import dataclass

name = "Server_Host"
client_list = []

# Creation of a Socket
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8081

# Binding the new socket
new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)


def client_adder():
    new_socket.listen(1)
    conn, add = new_socket.accept()

    print("Received connection from ", add[0])
    print('Connection Established. Connected From: ', add[0])

    client = (conn.recv(1024)).decode()
    print(client + ' has connected.')

    conn.send(name.encode())

    client_list.append((conn, add, client))

client_adder()
while True:
    message = input('Me : ')
    client_list[0][0].send(message.encode())
    message = client_list[0][0].recv(1024)
    message = message.decode()
    print(client_list[0][0], ':', message)