import socket 
from threading import Thread

SERVER = None
PORT = 8050
IP_ADDRESS = '127.0.0.1'
BUFFER_SIZE=4096
CLIENTS = {}

def setup():
    print("\n")
    print("\t\t\t\t\t\t*** SHARE MUSIC ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 8050
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")


    acceptConnections()

setup_thread=Thread(target=setup)
setup_thread.start()

def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        client, addr = SERVER.accept()
        print(client,addr)


