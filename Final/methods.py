import sys
import socket

def send_file(file,socket):
	try:
		size = os.path.getsize(file)
		with open(file, 'b') as f:
		    data = f.read()
	except:
		print(file + " is not your current working directory")

	try:
		socket.sendall((str(size)+":").encode('')) # first, send packet with size of file to check against corruption
		socket.sendall(data)
	except Exception as e:
		print(e);

	return 0


def rec_file(file,socket):
	while ":" not in socket.recv():
		size = socket.recv()
	recd = 0
	chunks = []
	while recd < size:
        chunk = self.sock.recv(4096)
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        recd += len(chunk)
	with open(file , 'xb') as f:
		f.write(b''.join(chunks))

	return 0


def send_dirs():
	return

def rec_dirs():
	return

### bibliography
 # https://docs.python.org/3.3/howto/sockets.html
 # https://stackoverflow.com/questions/25435212/is-there-a-way-to-check-whether-the-data-buffer-for-a-socket-is-empty-or-not-in
 # https://stackoverflow.com/questions/41382127/how-does-the-python-socket-recv-method-know-that-the-end-of-the-message-has-be
