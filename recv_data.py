import socket               # Import socket module

index = "seq2seq.ckpt-test-index"
data = "seq2seq.ckpt-test.data-00000-of-00001"
meta = "seq2seq.ckpt-test.meta"
workFiles = ["vocab20000.enc", "vocab20000.dec", "checkpoint", index, data, meta]

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
    for file in workFiles:
        f = open(file, 'wb')
        c, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        print "Receiving..."
        l = c.recv(1024)  # this receives 13 bytes which is corrupting the data
        l = c.recv(1024)
        while (l):
            print "Receiving..."
            f.write(l)
            l = c.recv(1024)
        f.close()
    print "Done Receiving"
    c.send('Thank you for connecting')
    c.close()                # Close the connection