import socket
import sys

####### TASKS
# receive port
# loop : read data from client , and print
# loop : read input , send client
# if EXIT client, or server, or error then close client

#################
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.bind(("", int(sys.argv[1])))
srv_sock.listen(5)

while True:
    cli_sock, cli_addr = srv_sock.accept()
    request = cli_sock.recv(1024)
    print(str(cli_addr) + ": " + request.decode('utf-8'))
    cli_sock.close()
