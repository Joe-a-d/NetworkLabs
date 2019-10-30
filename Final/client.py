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
	# Exit with a non-zero value, to indicate an error condition
	exit(1)


try:
	# Loop until either the server closes the connection or the user requests termination
	while True:

		try: ## sockets still missing as arguments
            if (sys.argv[3].lower() == "put"):
                send_file(sys.argv[4])
            elif (sys.argv[3]).lower() == "get"):
                rec_file(sys.argv[4])
            else :
                rec_dirs()
        except Exception as e:
            print(e)
            exit(1)


		# Then, read data from server and print on screen
		bytes_read = socket_to_screen(cli_sock, srv_addr_str)
		if bytes_read == 0:
			print("Server closed connection.")
			break

finally:

	cli_sock.close()

# Exit with a zero value, to indicate success
exit(0)
