import socket
import sys
from methods import *

# Create the socket on which the server will receive new connections
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    # creates a socket with port == argument passed on CLI
    srv_sock.bind(("0.0.0.0", int(sys.argv[1])))
    srv_sock.listen(5)
    srv_sock.settimeout(60)
except Exception as e:
    print("Invalid command or busy port (check below). Shutting down client...")
    print(e)
    exit(1)


while True: #outer lopp ; keep alive
    try:
        print("Connection for " + socket.gethostbyname("0.0.0.0") + " established on port  " + sys.argv[1]) # acknowledges connection
        print("Waiting for new client... ")


        cli_sock, cli_addr = srv_sock.accept()
        cli_addr_str = str(cli_addr)


        print("Client " + cli_addr_str + " connected.")

    except:
        print("Connection to client failed")
        exit(1)

    while True:
        try:
            hello = cli_sock.recv(100).split(b"#")
            buffer = hello[0]
            filename = hello[1]
        except:
            print("File not found")
            break
        if buffer.decode() == "1%":
            response = rec_file(cli_sock,filename)
        elif (buffer.decode() == "2%"):
            response = send_file(cli_sock,filename)

        break

# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)
