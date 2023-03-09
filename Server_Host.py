import threading
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
port = 14967

# Binding the new socket
new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)

def client_adder():
    while True:
        new_socket.listen(10)
        conn, (ipAddress, _) = new_socket.accept()
        conn.settimeout(0.5)
        client = (conn.recv(1024)).decode()
        print(client + ' has connected from', ipAddress)
        conn.send(name.encode())
        client_list.append(ConnectedClient(client, conn, ipAddress))

def message_receiver():
    while True:
        for client in client_list:
            try:
                message = client.Connection.recv(1024)
                message = message.decode()
                print(client.Name, ':', message)
            except Exception:
                pass

t1 = threading.Thread(target=client_adder)
t2 = threading.Thread(target=message_receiver)
t1.start()
t2.start()

@dataclass
class ConnectedClient:
    Name = ""
    Connection = None
    IpAddress = None

    def __init__(self, name, conn, ip):
         self.Name = name
         self.Connection = conn
         self.IpAddress = ip