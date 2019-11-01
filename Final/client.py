import socket
import sys
from methods import *


# Create the socket with which we will connect to the server
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The server's address is a tuple, comprising the server's IP address or hostname, and port number

try:
    srv_addr = (sys.argv[1], int(sys.argv[2]))
    srv_addr_str = str(srv_addr)
except:
    print(time(),"Invalid command. Shutting down client...",end="")
    exit(1)

try:
    print()
    print(time(),"Connecting to " + srv_addr_str + "... ")


    cli_sock.connect(srv_addr)

    print(time(),"Connected.")
except Exception as e:

    print(time(),"Exception: ", e , ";" , "  Failed to connect. ",end="")
    # Exit with a non-zero value, to indicate an error condition
    exit(1)


### CLI arguments parsing
try:
    filename = sys.argv[4]
    fileRequest = True
except:
    fileRequest = False
try:
    request = sys.argv[3].lower()
except:
    print(time(),"Request method not provided... Shutting down ")
    cli_sock.close()

if fileRequest:
    if (request == "put"):
        cli_sock.send(b'1%#' + bytes(filename, 'utf8'))
        put = send_file(cli_sock,filename)
    elif (request == "get"):
        cli_sock.send(b'2%#'+ bytes(filename, 'utf8'))
        get = rec_file(cli_sock, filename)
elif (request == "list") :
    cli_sock.send(b'3%#')
    list = rec_dirs(cli_sock)
else :
    print()
    print(time(),"Invalid Input")




# Exit with a zero value, to indicate success
exit(0)
