import threading
import time, socket, sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 14967

print('This is your IP address: ', ip)
server_host = input('Enter friend\'s IP address:')
name = input('Enter Friend\'s name: ')

socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, ' has joined...')

def recieve_message():
    while True:
        message = (socket_server.recv(1024)).decode()
        print(message)


def send_message():
    while True:
        message = input()
        socket_server.send(message.encode())


t1 = threading.Thread(target=recieve_message)
t2 = threading.Thread(target=send_message)
t1.start()
t2.start()
t1.join()
t2.join()

