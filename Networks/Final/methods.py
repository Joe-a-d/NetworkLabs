import sys
import os
from os import path
import socket
from datetime import datetime


def send_file(socket,file):
    try:
        size = path.getsize(file)
        with open(file, 'rb') as f:
            data = f.read()
    except Exception as e:
        print(time(),"Exception: ", e  , end="")
        socket.close()
        return 0

    try:
        socket.sendall(b'##start##'+str.encode(str(size)+"%%size%%") + data )
        return 0
    except Exception as e:
        print(time(),e,end="")
    return 1



def rec_file(socket,filename):
    data = socket.recv(100).split(b'##start##')
    if data[0] == b'' and len(data) > 1:
        recd = data[1]
    elif len(data) == 1:
        recd = data[0]
    try:
        data = recd.split(b"%%size%%")
        size = data[0].decode()
        recd = data[1]
    except Exception as e:
        print(time(),"  File not found",end="")
        return 1
    chunks = []
    chunks.append(recd)
    recd = len(recd)
    while recd < int(size):
        chunk = socket.recv(4096)
        recd += len(chunk)
        chunks.append(chunk)
    data = b"".join(chunks)

    try:
        with open(filename, 'xb') as f:
            f.write(data)
    except Exception as e:
        print(time(),e,end="")
        return 1

    if (int(size) == len(data)):
        return 0
    else:
        print(size)
        print()
        print(time(),"the file was corrupted during transfer",end="")
        return 1


def send_dirs(socket):
    try:
        dirs = os.listdir()
        size = str(len(dirs)).encode()
        data =""
        for dir in dirs:
            data+=dir+","
        data = data[:-1] #removes empty byte string
        socket.sendall(size + b'%%' + data.encode())
    except:
        print(time(),e,end="")

    return 0

def rec_dirs(socket):
    data = socket.recv(1094)
    data = data.split(b'%%')
    size = int(data[0].decode())
    dirs =[]
    dirs = data[1].split(b',')
    while len(dirs) < size: # loop handles interrupted stream
        data = socket.recv(1094)
        data = data.split(b',')
        data = [dir for dir in data if dir not in dirs ]
        dirs.extend(data)

    if len(dirs) != size:
        print()
        print(time(),"Something went wrong while processing your request. This listing is incomplete",end="")
        return 1

    pprint_dirs(dirs)


    return 0

def pprint_dirs(dirs):
    print()
    print(time() + "Directory Listing:")
    dirs.sort()
    for dir in dirs:
        print(dir.decode())

def time():
    time = datetime.now().strftime("%H:%M:%S")
    return "[ " + time + " ]  "


### bibliography
 # https://docs.python.org/3.3/howto/sockets.html
 # https://stackoverflow.com/questions/25435212/is-there-a-way-to-check-whether-the-data-buffer-for-a-socket-is-empty-or-not-in
 # https://stackoverflow.com/questions/41382127/how-does-the-python-socket-recv-method-know-that-the-end-of-the-message-has-be
