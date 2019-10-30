import sys
import socket

def send_file(file,socket):
	try:
		size = os.path.getsize(file)
		with open(file, 'b') as f:
		    data = f.read()
	except:
		print(file + " does not exist or is not your current working directory")

	try:
		socket.sendall(data)
	except Exception as e:
		print(e);

	return 0


def rec_file():
	return


def send_dirs():
	return

def rec_dirs():
	return
