import sys
import os
from os import path
import socket
### add print time for each print


def send_file(socket,file):
    try:
        size = path.getsize(file)
        with open(file, 'rb') as f:
            data = f.read()
    except Exception as e:
        print(e)
        print(file.decode() + " not found. Shutting down client")
        socket.close()
        return 0

    try:
        socket.sendall(str.encode(str(size)+"%%") + data )
        return 0
    except Exception as e:
        print(e)
    print(data)
    return 1



def rec_file(socket,filename):
    try:
        data = socket.recv(100).split(b"%%")
        size = data[0].decode()
        recd = data[1]
    except:
        print("File not found -> " + filename)
        return 1
    chunks = []
    chunks.append(recd)
    recd = len(recd)
    while recd < int(size):
        chunk = socket.recv(4096)
        recd += len(chunk)
        chunks.append(chunk)
    data = b"".join(chunks)

    print(size,len(data))

    try:
        filename = "new"
        with open(filename, 'xb') as f:
            f.write(data)
    except Exception as e:
        print(e)

    if (size == len(data)):
        return 0
    else:
        print(filename + " was corrupted during transfer")
        return 1


def send_dirs():
    return

def rec_dirs():
    return

### bibliography
 # https://docs.python.org/3.3/howto/sockets.html
 # https://stackoverflow.com/questions/25435212/is-there-a-way-to-check-whether-the-data-buffer-for-a-socket-is-empty-or-not-in
 # https://stackoverflow.com/questions/41382127/how-does-the-python-socket-recv-method-know-that-the-end-of-the-message-has-be
