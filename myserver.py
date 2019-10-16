import socket
import sys

####### TASKS
# receive port
# loop : read data from client , and print
# loop : read input , send client
# if EXIT client, or server, or error then close client

#################


###########BUGS
# the port seems to remain in use for a while if the program crashes.
#which causes a busy port error after script rerun
############

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.bind(("", int(sys.argv[1])))
srv_sock.listen(5)

while True:
    cli_sock, cli_addr = srv_sock.accept()
    connection = True
    while connection:
        request = cli_sock.recv(1024)
        if request == "EXIT":
            print("The client as terminated this connection")
            connection = False
        else:
            print( "Message from : " + str(cli_addr) + " " + request.decode("utf-8") )
            serverMessage = input()
            cli_sock.sendall(serverMessage.encode("utf-8"))

    cli_sock.close()
