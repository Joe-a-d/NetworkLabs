import sys
import os
from os import path
import socket
### add print time for each print

### PROTOCOL
###### 1 for sending
###### 2 for receiving

## First forget the size, test establishing a conmection of a known file size, read send, and close socket form client.
# Write to file with different name in server side, close connection. Report


def send_file(socket,file):
    try:
        size = path.getsize(file)
        with open(file, 'rb') as f:
            data = f.read()
    except Exception as e:
        print(e)
        print(file + " not found")

    try:
        socket.sendall(str.encode(str(size)+"%%") + data )
        print("SENT:: ", end="")
        print(str.encode(str(size)+"%%") + data)
        return 0
    except Exception as e:
        print(e)
    print(data)
    return 1



def rec_file(socket,filename):
    data = socket.recv(100).split(b"%%")
    print(data)
    size = data[0].decode()
    chunks = []
    recd = data[1]
    chunks.append(recd)
    recd = len(recd)
    while recd < int(size):
        chunk = socket.recv(4096)
        recd += len(chunk)
        chunks.append(chunk)
    data = b"".join(chunks)

    print(data)
    print(size,len(data))

    try:
        with open(filename, 'xb') as f:
            f.write(data)
    except Exception as e:
        print(e)

    return (size, data)


def send_dirs():
    return

def rec_dirs():
    return

### bibliography
 # https://docs.python.org/3.3/howto/sockets.html
 # https://stackoverflow.com/questions/25435212/is-there-a-way-to-check-whether-the-data-buffer-for-a-socket-is-empty-or-not-in
 # https://stackoverflow.com/questions/41382127/how-does-the-python-socket-recv-method-know-that-the-end-of-the-message-has-be
