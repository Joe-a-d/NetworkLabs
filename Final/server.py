import socket
import sys
from methods import *

# Create the socket on which the server will receive new connections
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 120

try:
    # creates a socket with port == argument passed on CLI
    srv_sock.bind(("0.0.0.0", int(sys.argv[1])))
    srv_sock.listen(5)
    srv_sock.settimeout(timeout)
except Exception as e:
    print(time(),e, end="")
    exit(1)


while True: #outer lopp ; keep alive
    try:
        print()
        print(time(),"Connection for " + socket.gethostbyname("0.0.0.0") + " established on port  " + sys.argv[1]) # acknowledges connection
        print(time(),"Server Timeout Set to : " + str(timeout) + "s")
        print(time(),"Waiting for new client... ")


        cli_sock, cli_addr = srv_sock.accept()
        cli_addr_str = str(cli_addr)

        print()
        print(time(),"Client " + cli_addr_str + " connected.")

    except Exception as e:
        print(time(),"Exception: ", e , ";" , "  Connection to client failed" , end ="")
        exit(1)

    while True:
        try:
            hello = cli_sock.recv(100).split(b"#")
            buffer = hello[0]
            filename = hello[1]
            print(hello)
        except:
            print(time(),"File not found sa")
            break
        if buffer.decode() == "1%":
            response = rec_file(cli_sock,filename)
        elif (buffer.decode() == "2%"):
            response = send_file(cli_sock,filename)
        elif (buffer.decode() == "3%"):
            response = send_dirs(cli_sock)

        if not response:
            print("REQUEST : OK")

        break



# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)
