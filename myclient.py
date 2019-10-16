import socket
import sys

###### TASKS
# Args : hostname , port number
# Read input from command line, and send when \n
# Read server response and output
# Stop when input from server or output from client == 'EXIT'
#### if server exited , i.e. if server == exit, then print diagnostic message
##############
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_sock.connect((sys.argv[1], int(sys.argv[2])))

connected = True
while connected:
    clientMessage = str(input())
    cli_sock.sendall(clientMessage.encode("utf-8"))
    if clientMessage == "EXIT":
        connected = False
        cli_sock.sendall(clientMessage.encode("utf-8"))
        cli_sock.close()
    else:
        response = cli_sock.recv(1024)
        print("Server Response: " + " " + response.decode("utf-8"))
        if response == "EXIT":
            connected = False
