import socket
import sys
from methods import *


# Create the socket with which we will connect to the server
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The server's address is a tuple, comprising the server's IP address or hostname, and port number

srv_addr = (sys.argv[1], int(sys.argv[2]))

# Convert to string
srv_addr_str = str(srv_addr)


try:
    print("Connecting to " + srv_addr_str + "... ")


    cli_sock.connect(srv_addr)

    print("Connected.")
except Exception as e:
    # Print the exception message
    print(e)
    print('connect client broke') #debug
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
    print("Request method not provided... Shutting down ")
    cli_sock.close()

if fileRequest:
    if (request == "put"):
        cli_sock.send(b'1%#' + bytes(filename, 'utf8'))
        put = send_file(cli_sock,filename)
    elif (request == "get"):
        cli_sock.send(b'2%#'+ bytes(filename, 'utf8'))
        get = rec_file(cli_sock, filename)
elif (request == "list") :
    list = rec_dirs()
else :
    print("Invalid Input")




# Exit with a zero value, to indicate success
exit(0)
