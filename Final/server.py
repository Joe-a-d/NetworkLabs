import socket
import sys
from lab3 import socket_to_screen, keyboard_to_socket

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


while True:

	try:
        print("Connection for " + socket.gethostbyname("0.0.0.0") + " established on port  " + sys.argv[1]) # acknowledges connection
		print("Waiting for new client... ")


		cli_sock, cli_addr = srv_sock.accept()
		cli_addr_str = str(cli_addr) # Translate the client address to a string


		print("Client " + cli_addr_str + " connected.")

		# Loop until either the client closes the connection or the user requests termination
		while True:
			# First, read data from client and print on screen
			bytes_read = socket_to_screen(cli_sock, cli_addr_str)
			if bytes_read == 0:
				print("Client closed connection.")
				break

			# Then, read data from user and send to client
			bytes_sent = keyboard_to_socket(cli_sock)
			if bytes_sent == 0:
				print("User-requested exit.")
				break

	finally:

		cli_sock.close()

# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)
