import multiprocessing
import time, socket
from dataclasses import dataclass

name = "Server_Host"
client_list = []
last_client = ""
last_message = ""
# Creation of a Socket
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 14968

# Binding the new socket
new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)


def client_adder():
    while True:
        new_socket.listen(10)
        conn, add = new_socket.accept()
        print('test')

        print("Received connection from ", add[0])
        print('Connection Established. Connected From: ', add[0])

        client = (conn.recv(1024)).decode()
        print(client + ' has connected.')

        conn.send(name.encode())

        client_list.append((conn, add, client))


def chat_loop():
    global last_client, last_message
    for client in client_list:
        if client != last_client:
            client[0].send(last_message.encode())


def message_receiver():
    global last_client, last_message
    while True:
        for client in client_list:
            message = client[0].recv(1024)
            message = message.decode()
            print(client[2], ':', message)
            last_client = client
            last_message = message


t1 = multiprocessing.Process(target=client_adder)
t2 = multiprocessing.Process(target=message_receiver)

t1.start()
t2.start()
