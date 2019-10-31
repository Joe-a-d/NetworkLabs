import socket
import sys
from methods import *

# Create the socket on which the server will receive new connections
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    # creates a socket with port == argument passed on CLI
    srv_sock.bind(("0.0.0.0", int(sys.argv[1])))


    # accepts a max of 5 connections
    srv_sock.listen(5)
except Exception as e:

    print(e)
    # Exit with a non-zero value, to indicate an error condition
    exit(1)

i=0
while True: #outer lopp ; keep alive
    try:
        print("Connection for " + socket.gethostbyname("0.0.0.0") + " established on port  " + sys.argv[1]) # acknowledges connection
        print("Waiting for new client... ")


        cli_sock, cli_addr = srv_sock.accept()
        cli_addr_str = str(cli_addr)


        print("Client " + cli_addr_str + " connected.")

        while True:
            hello = cli_sock.recv(100).split(b"#")
            buffer = hello[0]
            filename = hello[1]
            print("FIRST BUFFER",end="")
            print(hello)
            if buffer.decode() == "1%":
                print("PUT RECEIVED, WAITING FOR FILE SIZE") #debug
                response = rec_file(cli_sock,filename)
            elif (buffer.decode() == "2%"):
                print("GET RECEIVED")
                response = send_file(cli_sock,filename)

            break




    finally:

        cli_sock.close()

# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)
