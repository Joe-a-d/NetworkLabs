import socket                   # Import socket module

try:
    port = 3000
except:
    port= 2000                 # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    buffer = conn.recv(1024)
    print('Server received', repr(buffer))
    buffer = buffer.split(b"%%")
    request = buffer[0]
    filename = buffer[1]
    print(request,filename)

    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()
